import streamlit as st
import gtts
import os
import speech_recognition as sr
from groq import Groq
import tempfile
import pydub
from dotenv import load_dotenv
from pydub.utils import which

load_dotenv()
api_keys = st.secrets["api"]  # Securely load API key from Streamlit secrets

# Set the ffmpeg path for pydub
pydub.AudioSegment.converter = which("ffmpeg")

# Initialize Groq client
client = Groq(api_key=api_keys)

# Function to convert audio file to WAV format
def convert_audio_to_wav(audio_path):
    audio = pydub.AudioSegment.from_file(audio_path)
    wav_path = "converted_audio.wav"
    audio.export(wav_path, format="wav")
    return wav_path

# Function to transcribe audio using speech recognition
def transcribe_audio(audio):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        st.warning("I didn't catch that. Please respeak.")
        return None
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")
        return None

# Function to get LLM response from Groq API
def generate_response(text):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": text}],
        model="llama3-8b-8192",
    )
    response = chat_completion.choices[0].message.content
    return response

# Function to convert LLM response text to speech
def text_to_speech(text):
    tts = gtts.gTTS(text)
    audio_path = "response.mp3"
    tts.save(audio_path)
    return audio_path

# Streamlit application
st.title("Voice-to-Voice Interaction")
st.subheader("Chat with Voice Input")

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Function to display chat history
def display_chat():
    for user_input, response in st.session_state.chat_history:
        st.write(f"<div style='text-align: right; color: blue;'>**User:** {user_input}</div>", unsafe_allow_html=True)
        st.write(f"<div style='text-align: left; color: green;'>**Response:** {response}</div>", unsafe_allow_html=True)

# Part 1: Audio or Microphone Input
st.header("Input Audio or Speak")
input_option = st.radio("Choose Input Method", options=["Upload Audio File", "Use Microphone"])

if input_option == "Upload Audio File":
    uploaded_audio = st.file_uploader("Upload Audio", type=["wav", "mp3"])
    if uploaded_audio is not None:
        with tempfile.NamedTemporaryFile(delete=False) as temp_audio_file:
            temp_audio_file.write(uploaded_audio.read())
            temp_audio_file.close()
        
        # Convert to WAV format if necessary
        converted_audio_
