import os
import requests
import time

def transcribe(audio_content):
    api_key = os.getenv("ASSEMBLYAI_API_KEY")
    if not api_key:
        return {"text": "STT Error: API Key missing", "provider": "assemblyai"}

    headers = {
        "authorization": api_key,
        "content-type": "application/json"
    }

    # Step 1: Upload the audio
    upload_url = "https://api.assemblyai.com/v2/upload"
    response = requests.post(upload_url, headers=headers, data=audio_content)
    
    if response.status_code != 200:
        return {"text": f"STT Error: Upload failed ({response.status_code})", "provider": "assemblyai"}
    
    upload_url = response.json()["upload_url"]

    # Step 2: Request transcription
    transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
    json_data = {"audio_url": upload_url}
    response = requests.post(transcript_endpoint, json=json_data, headers=headers)
    
    if response.status_code != 200:
        return {"text": f"STT Error: Transcription request failed", "provider": "assemblyai"}
    
    transcript_id = response.json()["id"]
    polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"

    # Step 3: Polling for results
    while True:
        polling_response = requests.get(polling_endpoint, headers=headers)
        status = polling_response.json()["status"]

        if status == "completed":
            return {
                "text": polling_response.json()["text"],
                "provider": "assemblyai",
                "id": transcript_id
            }
        elif status == "error":
            return {"text": f"STT Error: {polling_response.json().get('error')}", "provider": "assemblyai"}
        
        time.sleep(1)
