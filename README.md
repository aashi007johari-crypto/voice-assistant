# voice-assistant
A Python-based voice assistant that can perform basic tasks using voice commands. It listens for the wake word **"Jarvis"** and responds to user commands.

## Features

- Voice activation using "Jarvis"
- Open Google, YouTube, Instagram, and LinkedIn
- Search and play songs on YouTube
- Read the latest news headlines
- Generate AI-based responses using SambaNova AI (Llama 3.3 70B)
- Convert text responses to speech

## Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- OpenAI Python SDK (SambaNova API)
- Feedparser

## How to Run

1. Clone this repository.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your own SambaNova API key.
4. Run:
   ```bash
   python main.py
   ```

## Note

This project requires a working microphone and an active internet connection for speech recognition, AI responses, and news updates.

## Author

**Aashi**
