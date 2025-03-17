import openai
import os
import requests
import json
from io import BytesIO
import langid

from openai.types.audio import Translation

# API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVEN_LABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Initialize OpenAI client
openai.api_key = OPENAI_API_KEY

def transcribe_audio(file_path):
    """Transcribe an audio file using OpenAI Whisper API."""
    with open(file_path, "rb") as audio_file:
        response = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"
        )


    return response


def translation(text):
    language, _ = langid.classify(text)
    if language == "en":
        return text
    else:
        prompt = f"Translate the following text into English and return only translation nothing else.:\n\n{text}\n\nTranslation:"

        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional Translator to English."},
                {"role": "user", "content": prompt}
            ]
        )

        Translation_response = response.choices[0].message.content
        return Translation_response


def accent_change(text):
    """Convert text to American accent using GPT-4."""
    prompt = f"Convert the following text into an American-accented pronunciation style without changing the sentence structure:\n\n{text}\n\nAmerican Accent Version:"

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional American English speech."},
            {"role": "user", "content": prompt}
        ]
    )

    american_response = response.choices[0].message.content
    print(f"Original: {text}")
    print(f"American: {american_response}")
    return american_response

def text_to_speech_elevenlabs(text):
    """Convert text to speech using ElevenLabs API without using the Python SDK."""
    url = "https://api.elevenlabs.io/v1/text-to-speech/9BWtsMINqrJLrRacOk9x"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVEN_LABS_API_KEY
    }

    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.6,
            "similarity_boost": 0.65
        }
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        print(f"Error with ElevenLabs API: {response.status_code} - {response.text}")
        raise Exception(f"ElevenLabs API error: {response.status_code}")

