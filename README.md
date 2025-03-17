# Supportiyo AI - Speech Accent Enhancer

Transform your speech in real-time with an American accent!
![image](https://github.com/user-attachments/assets/56434e15-4e36-4b2d-ae95-e6b4f200607a)

---

## 📖 Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation Guide](#installation-guide)
- [How to Use](#how-to-use)
- [Demo](#demo)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## 📝 Introduction

Supportiyo AI is a cutting-edge tool designed to enhance your speech with a real-time American accent. Powered by advanced technologies such as OpenAI’s Whisper API for speech-to-text, GPT-4 for accent conversion, and ElevenLabs for text-to-speech, it provides an intuitive and seamless experience. This tool also features automatic translation, making non-English speech easily understandable in English.

---

## 🚀 Features

- **Real-time Accent Enhancement** – Speak and instantly hear your speech transformed with an American accent.
- **Speech-to-Text (STT)** – Transcribes your speech using OpenAI’s Whisper API.
- **Translation** – Automatically translates non-English speech into English.
- **Accent Conversion** – Changes your speech to a natural-sounding American accent using GPT-4.
- **Text-to-Speech (TTS)** – Converts your text into high-quality speech with ElevenLabs API.
- **User-Friendly Interface** – Simple and interactive web UI for easy usage.

---

## 🛠️ Technologies Used

### Backend
- **Python** – A popular language for building server-side applications.
- **Flask** – A lightweight web framework for Python.
- **OpenAI API** – Utilizing Whisper for speech-to-text and GPT-4 for accent conversion.
- **ElevenLabs API** – Powers high-quality text-to-speech functionality.
- **Additional Libraries**:
  - `soundfile` – For handling audio files.
  - `langid` – For detecting the language of the speech.
  - `python-dotenv` – For managing environment variables securely.

### Frontend
- **HTML** – For structuring the web interface.
- **CSS** – For styling the web pages.
- **JavaScript** – For interactive elements and handling front-end logic.

---

## ⚡ Installation Guide

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-repo-url.git
cd Supportivo-AI-Accent-Enhancer
```

### 2️⃣ Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up API keys
Create a `.env` file in the project root and add your API keys:
```bash
OPENAI_API_KEY=your_openai_key
ELEVENLABS_API_KEY=your_elevenlabs_key
```

### 5️⃣ Run the Flask app
```bash
python app.py
```

### 6️⃣ Access the web app
Open your browser and visit [http://localhost:5000](http://localhost:5000) to start using the application.

---

## 🎯 How to Use

1. **Click the 🎤 microphone icon** to start recording.
2. **Speak into your microphone** to capture your speech.
3. **Click ⏹️ stop** to finish the recording.
4. View the **transcribed and enhanced speech** on the interface.
5. **Press ▶️ play** to hear your speech with the transformed American accent.

---

## 🎥 Demo

You can watch the demo of the application in action here:  
**[Demo URL goes here]**

---

## 🛠️ Troubleshooting

- **Error: API Key Missing or Incorrect**  
  Make sure that your `.env` file contains the correct `OPENAI_API_KEY` and `ELEVENLABS_API_KEY`. Check for any typos or missing keys.

- **Microphone Not Working**  
  Ensure that your browser has the necessary permissions to access your microphone. Check that the microphone is correctly set up on your system.

- **Audio Quality Issues**  
  If you're experiencing poor audio quality, verify your internet connection speed and ensure the APIs are properly responding.

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

--- 

This README provides a thorough and easy-to-follow guide for setting up and using **Supportiyo AI - Speech Accent Enhancer**.
