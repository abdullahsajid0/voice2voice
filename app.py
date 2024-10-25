import os
import whisper
from groq import Groq
from gtts import gTTS
import gradio as gr
import tempfile

# Load the whisper model
whisper_model = whisper.load_model("base")


# Access the secret
api_key = os.getenv("GROQ_API_KEY")


# Set your API key for Groq
#os.environ['GROQ_API_KEY'] = 'your_groq_api_key'  # Replace with your actual key

# Function to transcribe audio
def transcribe_audio(audio_file):
    try:
        result = whisper_model.transcribe(audio_file)
        return result['text']
    except Exception as e:
        return f"Error during transcription: {e}"

# Function to interact with Groq's language model
def chat_with_groq(user_input):
    try:
        client = Groq(api_key=os.getenv('GROQ_API_KEY'))
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": user_input}],
            model="llama3-8b-8192"
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error interacting with LLM: {e}"

# Function to convert text to speech
def text_to_speech(text):
    try:
        tts = gTTS(text=text, lang='en')
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)
        return temp_file.name
    except Exception as e:
        return f"Error during text-to-speech conversion: {e}"

# Main function to process audio input
def process_audio(audio):
    transcription = transcribe_audio(audio)
    if "Error" in transcription:
        return None, transcription  # Return transcription error message

    response = chat_with_groq(transcription)
    if "Error" in response:
        return None, response  # Return LLM error message

    audio_response = text_to_speech(response)
    if not audio_response:
        return None, "Error generating audio response"

    return audio_response, None  # Return audio and no error message

# Gradio interface setup
interface = gr.Interface(
    fn=process_audio,
    inputs=gr.Audio(type="filepath", label="Upload your audio file"),
    outputs=[gr.Audio(type="filepath", label="Bot's Response"), gr.Textbox(label="Message")],
    title="Voice-to-Voice AI Assistant",
    description="Speak to the bot, and it will respond with a voice message!",
    theme="default"  # Change the theme as needed
)

# Launch the Gradio app
interface.launch(inbrowser=True)
