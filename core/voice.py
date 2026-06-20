import os
import tempfile
from groq import Groq


def get_groq_client():
    """Reuse same Groq client setup"""
    try:
        env_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), '.env'
        )
        with open(env_path) as f:
            for line in f:
                if line.startswith('GROQ_API_KEY='):
                    key = line.strip().split('=', 1)[1]
                    return Groq(api_key=key)
    except Exception as e:
        print(f"Voice API key error: {e}")
    return None


def transcribe_audio(audio_bytes):
    """
    Transcribe voice recording using Groq's Whisper API.
    Free, fast, supports Hindi/Kannada/Tamil natively.
    """
    try:
        client = get_groq_client()
        if not client:
            return None, "API key not found"

        # Save audio to temp file
        with tempfile.NamedTemporaryFile(
            suffix=".wav", delete=False
        ) as tmp_file:
            tmp_file.write(audio_bytes)
            tmp_path = tmp_file.name

        # Transcribe using Groq Whisper
        with open(tmp_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-large-v3-turbo",
                response_format="text"
            )

        os.unlink(tmp_path)  # cleanup temp file

        return str(transcription).strip(), None

    except Exception as e:
        print(f"Transcription error: {e}")
        return None, str(e)