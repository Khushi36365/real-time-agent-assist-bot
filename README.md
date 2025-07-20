# 🎧 Real-Time Agent Assist Bot

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-brightgreen)
![Whisper](https://img.shields.io/badge/Whisper-SpeechToText-purple)

---

## 🎯 Overview
The **Real-Time Agent Assist Bot** is an AI-powered tool designed to help customer support agents by:
- Converting **audio (recorded or uploaded) to text** in real time using **Whisper**
- Detecting the **intent** of the query using rule-based logic (or GPT if enabled)
- Providing **smart response suggestions** to assist agents

This solution enhances **response time**, **accuracy**, and **customer experience**.

---

## 🚀 Features
✔ Upload an audio file **or** record live audio  
✔ **Real-time transcription** with Whisper  
✔ **Intent detection** (via rule-based logic, no API required)  
✔ Smart **predefined responses** for common issues  
✔ **Interactive Streamlit UI** with progress indicators  

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit** for UI
- **Whisper** for speech-to-text
- **Rule-based intent detection**

---

## 📂 Project Structure
```

real-time-agent-assist-bot/
│
├── app/
│   ├── backend/
│   │   └── transcription.py         # Audio transcription logic
│   ├── models/
│   │   └── intent\_detection.py      # Intent detection using rules
│   └── frontend/
│       └── ui.py                    # Streamlit UI
│
├── data/
│   └── sample\_audio.wav             # Sample audio file
│
├── README.md
└── requirements.txt

````

---

## ⚡ Setup Instructions
### 1. Clone this repo
```bash
git clone https://github.com/YOUR-USERNAME/real-time-agent-assist-bot.git
cd real-time-agent-assist-bot
````

### 2. Create Virtual Environment & Activate

```bash
python -m venv venv
venv\Scripts\activate    # Windows
# OR
source venv/bin/activate # Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app/frontend/ui.py
```

---

## 🔥 Future Enhancements

* ✅ **Auto-Summarization** of transcript
* ✅ **Confidence Score** for detected intent
* ✅ **Multi-language Support**

---

## 👩‍💻 Author

### **Khushi**

📌 [LinkedIn](https://www.linkedin.com/in/khushi-jhamb/) 

📌 [GitHub](https://github.com/Khushi36365)
