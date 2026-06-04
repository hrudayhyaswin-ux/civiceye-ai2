# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

import os

from google import genai
from google.genai import types


def transcribe_with_gemini(audio_content, mime_type="audio/webm"):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return {"text": "STT Error: GEMINI_API_KEY missing", "provider": "gemini"}

    try:
        client = genai.Client(api_key=api_key)

        # We can pass the audio bytes directly to the model
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[
                types.Part.from_bytes(data=audio_content, mime_type=mime_type),
                "Please transcribe this audio accurately. If it's in a language other than English, provide the transcription in that language."
            ]
        )

        return {
            "text": response.text,
            "provider": "gemini"
        }
    except Exception as e:
        return {"text": f"STT Error: {str(e)}", "provider": "gemini"}
