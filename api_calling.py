from google import genai
import os
from dotenv import load_dotenv
import streamlit as st
from gtts import gTTS
import io

load_dotenv()

api_key = os.environ.get("GOOGLE_GEMINI_KEY")
# api_key = os.getenv("GOOGLE_GEMINI_KEY")

client = genai.Client(api_key = api_key)

#note generator

def note_generator(images):
    prompt = """Summarize the picture in note format at max 100 words, make sure to add necessary markdown to differentiate different section"""

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images, prompt]
    )
    return response.text

def audio_transcription(text):
    speech = gTTS(text,lang = "en", slow = False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer


def quiz_generator(images, difficulty):
    prompt = f"Generate 3 quizzes based on {difficulty}. Make sure to add necessary markdown to differentiate different section"

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images, prompt]
    )
    return response.text