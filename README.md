# 🎙️ AI Text-to-Speech Desktop Application

## 📌 Overview

This project is a **GUI-based AI Text-to-Speech (TTS) Desktop Application** built using **Python and Tkinter**.
It allows users to convert text into speech with multilingual support, file reading, clipboard reading, and MP3 audio saving features.

The application provides an easy-to-use and modern interface for real-time speech generation and control.

---


## ✨ Features

### 🔊 Speech Features

* Default text-to-speech using offline engine
* Multilingual speech support
* Automatic language detection
* Adjustable speech rate
* Voice selection

### ⏯️ Playback Controls

* Pause speech
* Resume speech
* Stop speech
* Real-time control using threading

### 📂 File & Input Support

* Read text from clipboard
* Open and read text files
* Open and extract text from PDF files
* Multilingual support for file content

### 💾 Audio Export

* Save speech as MP3 file

### 🎨 GUI

* Modern and responsive Tkinter interface
* Hover button effects
* User-friendly layout

---

## 🛠️ Technologies Used

* Python
* Tkinter (GUI)
* pyttsx3 (Offline TTS)
* gTTS (Google Text-to-Speech)
* langdetect
* PyPDF2
* threading
* playsound
* pyperclip

---

## 📦 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Koushik07-c/text-to-speech
cd AI-Text-To-Speech-App
```

### Step 2: Install Required Libraries

```bash
pip install pyttsx3 tkinter langdetect gTTS playsound pyperclip PyPDF2
```

---

## ▶️ Usage

Run the Python file:

```bash
python text_to_speech.py
```

---

## 📖 How to Use

1. Enter text in the text area.
2. Select voice and speech rate.
3. Click:

   * **Speak (Default)** → Offline speech
   * **Speak (Multilingual)** → Auto language detection
4. Use playback controls to pause, resume, or stop speech.
5. Open text or PDF files for reading.
6. Save audio as MP3.

---

## 🔐 Advantages

* Works offline for default speech
* Supports multiple languages
* Simple and interactive interface
* Supports file-based and real-time speech
* Suitable for accessibility and learning applications

---

## 🚀 Future Enhancements

* AI voice cloning
* Emotion-based speech
* Mobile and web versions
* Speech-to-text integration
* Cloud storage support
* Dark/light mode

---

## 🤝 Contribution

Contributions are welcome!
Feel free to fork this repository and submit pull requests.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Developed by **Koushik S V**

---
