# apna-project
# Voice-Driven Banking via LAMs (C4GT 2025 Proposal)

This repository contains the early-stage prototype for the "Voice-Driven Banking using LLMs" project under Mifos for C4GT 2025.

## 🔍 Project Objective

Leverage open-source STT (Speech-to-Text) and TTS (Text-to-Speech) tools to enable voice-driven banking experiences for underserved users via conversational interfaces powered by LLMs.

## 💡 Features

- Simulated voice input/output flow
- Placeholder for integration with Whisper/Vosk STT engine
- Simple conversational interface for mock banking queries
- Modular code for future LLM API integration (LLAMA2/OpenChat)

## 📦 Structure

```
.
├── README.md
├── app.py              # Main Flask app
├── templates/
│   └── index.html      # UI for the voice interaction demo
├── static/
│   └── style.css       # Basic styles
└── voice/
    └── mock_stt.py     # Simulated STT processor (placeholder)
```

## 🚀 Future Plans

- Integrate actual Whisper or Vosk STT module
- Add real-time TTS response (pyttsx3 or gTTS)
- Connect to sample banking APIs for real use-cases
- Add Hindi & Telugu language support
