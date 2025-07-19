import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import streamlit as st
from streamlit_mic_recorder import mic_recorder
from app.backend.transcription import transcribe_audio
from app.models.intent_detection import detect_intent
import time

# --- Page Config ---
st.set_page_config(page_title="Agent Assist Bot", page_icon="🎧", layout="centered")

# --- Title & Description ---
st.title("🎧 Real-Time Agent Assist Bot")
st.markdown("**Boost customer support efficiency with real-time transcription, intent detection, and smart responses.**")

# --- Tabs for Upload and Record ---
tab1, tab2 = st.tabs(["📂 Upload Audio", "🎤 Record Audio"])

audio_path = None

with tab1:
    uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
    if uploaded_file:
        audio_path = "temp_audio.wav"
        with open(audio_path, "wb") as f:
            f.write(uploaded_file.read())
        st.success("✅ Audio uploaded successfully!")

with tab2:
    st.markdown("Click below to record:")
    recorded_audio = mic_recorder(
        start_prompt="🎤 Start Recording",
        stop_prompt="⏹ Stop Recording",
        just_once=True
    )
    if recorded_audio:
        audio_path = "temp_audio.wav"
        with open(audio_path, "wb") as f:
            f.write(recorded_audio["bytes"])
        st.success("✅ Recording saved successfully!")

# --- Processing Section ---
if audio_path:
    st.info("⏳ Processing your audio...")
    progress = st.progress(0)
    
    start_time = time.time()
    transcript = transcribe_audio(audio_path)
    progress.progress(50)

    intent = detect_intent(transcript)
    progress.progress(80)

    transcription_time = round(time.time() - start_time, 2)
    progress.progress(100)

    st.subheader("📝 Transcript")
    st.write(transcript)

    st.subheader("🎯 Detected Intent")
    st.success(f"**{intent}**")

    st.subheader("💡 Suggested Response")
    solutions = {
        "Password Reset": "Guide the user to reset their password via self-service portal.",
        "Account Locked": "Help the user unlock their account using OTP verification.",
        "Billing Issue": "Direct the user to the billing help page or escalate to finance team.",
        "Refund Request": "Inform the user about refund policy and initiate request.",
        "Order Inquiry": "Provide the current order status from the system.",
        "Delivery Status": "Update the user about expected delivery date."
    }
    if intent in solutions:
        st.write(f"✅ {solutions[intent]}")
    else:
        st.warning("⚠ No predefined solution found. Escalate to agent.")

    # Metrics
    st.caption(f"⏱ **Transcription Time:** {transcription_time} sec")
