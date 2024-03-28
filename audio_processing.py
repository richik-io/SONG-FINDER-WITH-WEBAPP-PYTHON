# audio_processing.py
from pydub import AudioSegment
import os

def convert_to_wav(uploaded_file):
    # Convert MP3 to WAV
    audio = AudioSegment.from_file(uploaded_file)
    wav_file = uploaded_file.name.replace(".mp3", ".wav")
    audio.export(wav_file, format="wav")
    return wav_file
