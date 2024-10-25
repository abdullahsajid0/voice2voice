# Voice-to-Voice AI Assistant

This Voice-to-Voice AI Assistant enables seamless, real-time interactions with an AI, allowing users to upload an audio file, receive a transcription, interact with a language model, and get a spoken response back. This project is built using OpenAI’s Whisper for transcription, Groq's LLM for text generation, gTTS for text-to-speech conversion, and Streamlit for deployment.

## Demo

You can try the application here: [Live Project Link](https://huggingface.co/spaces/abdullahsajid0/voice2voice)

## Features

- **Automatic Speech Recognition (ASR)**: Converts audio to text using OpenAI’s Whisper.
- **Conversational AI**: Engages in conversation with Groq's advanced LLM.
- **Text-to-Speech (TTS)**: Transforms AI responses into speech using gTTS.
- **User-Friendly UI**: Built with Streamlit for an intuitive user experience.

## Project Structure

```bash
.
├── app.py             # Main Streamlit app code
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
```
# Getting Started

- Python 3.8 or higher
- [Whisper by OpenAI](https://github.com/openai/whisper)
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)
- [Groq API access](https://groq.com) and API Key

# Installation
 1.  ### Clone the repository:
```bash
   git clone https://github.com/abdullahsajid0/voice2voice.git
   cd voice2voice
 ```
1. Install dependencies:

```
pip install -r requirements.txt
```
2. ### Set up the Groq API Key:

Export your API key to the environment:


```
export GROQ_API_KEY="your_groq_api_key"
```
3. ### Run the Gradio app:

```
python app.py
```
## Usage
1. Open the app in your browser (usually at http://localhost:7860).
2. Upload an audio file in .wav, .mp3, or .ogg format.
3. The app transcribes the audio, interacts with the language model, and returns an audio response that you can listen to directly on the platform.
## Technology Stack
- Whisper: Automatic speech recognition
- Groq: LLM-based conversation model
- gTTS: Text-to-speech
- Gradio: Web-based interface
## Dependencies
- The main dependencies are included in requirements.txt:

```txt 
whisper==1.0
groq==1.1
gtts==2.3.2
gradio==3.16.0```
Install these via:
```
```
pip install -r requirements.txt
```
