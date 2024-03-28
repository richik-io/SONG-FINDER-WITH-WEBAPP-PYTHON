# streamlit_app.py
import streamlit as st
from app.audio_processing import convert_to_wav
from app.audio_transcription import transcribe_audio
from app.language_model import generate_response

def main():
    st.title("Audio Transcription and Question Answering")

    # File upload
    uploaded_file = st.file_uploader("Upload an audio file (MP3 or WAV)", type=["mp3", "wav"])

    if uploaded_file:
        # Convert audio to WAV
        wav_file = convert_to_wav(uploaded_file)
        
        # Display uploaded audio
        st.audio(wav_file, format='audio/wav')

        # Transcription
        st.subheader("Transcription:")
        transcription = transcribe_audio(wav_file)
        st.write(transcription)

        # Question answering
        question = st.text_input("Ask a question about the audio:")
        if question:
            # Generate prompt for Gen AI
            prompt = f"Audio transcription: {transcription}. Question: {question}"
            answer = generate_response(prompt)
            st.write("Answer:", answer)

if __name__ == "__main__":
    main()
