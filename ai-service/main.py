# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

import json
import os

from fastapi import FastAPI, File, Form, UploadFile
from models.classify_complaint import classify
from models.detect_entities import detect_entities
from models.duplicate_checker import duplicate_confidence
from models.prioritize_issue import prioritize
from providers.assemblyai_client import transcribe as transcribe_assembly
from providers.gemini_client import transcribe_with_gemini
from pydantic import BaseModel, Field

app = FastAPI(title="CivicEye AI Service")

def transcribe(content):
    if os.getenv("GEMINI_API_KEY"):
        return transcribe_with_gemini(content)
    elif os.getenv("ASSEMBLYAI_API_KEY"):
        return transcribe_assembly(content)
    else:
        return {"text": "No STT provider configured (need GEMINI_API_KEY or ASSEMBLYAI_API_KEY)", "provider": "none"}


class ComplaintPayload(BaseModel):
    title: str = ""
    description: str = ""
    category_hint: str = "Other"
    location: dict = Field(default_factory=dict)
    language: str = "en"


@app.get("/health")
def health():
    return {"status": "healthy", "service": "civiceye-ai"}


@app.post("/analyze")
async def analyze(
    payload: str | None = Form(None),
    voice_note: UploadFile | None = File(None),
    json_payload: ComplaintPayload | None = None
):
    if payload:
        data = ComplaintPayload(**json.loads(payload))
    elif json_payload:
        data = json_payload
    else:
        data = ComplaintPayload()

    description = data.description

    if voice_note:
        # Save or process voice note
        content = await voice_note.read()
        # For now, we'll use a mock transcription or actual one if implemented
        # In a real scenario, we'd upload to a bucket or send to STT
        transcript_data = transcribe(content)
        if transcript_data.get("text"):
            description += f"\n\n[Voice Transcript]: {transcript_data['text']}"

    category, department = classify(data.category_hint, description)
    entities = detect_entities(description, data.location)
    priority = prioritize(data.title, description, category)
    duplicate = duplicate_confidence(description)
    summary = summarize(description, entities)

    return {
        "category": category,
        "department": department,
        "priority": priority,
        "summary": summary,
        "duplicate_confidence": duplicate,
        "entities": entities,
        "transcript": transcript_data.get("text") if voice_note else None
    }


def summarize(description, entities):
    text = description.strip()
    if len(text) > 180:
        text = f"{text[:177]}..."
    landmark = entities.get("landmark")
    return f"{text} Location signal: {landmark}." if landmark else text

