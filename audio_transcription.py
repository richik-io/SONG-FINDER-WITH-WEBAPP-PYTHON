# audio_transcription.py
from pydub import AudioSegment
import speech_recognition as sr

def transcribe_audio(audio_file_path):
    # Load audio file using pydub
    audio = AudioSegment.from_file(audio_file_path)

    # Export audio as WAV (required format for speech_recognition)
    wav_file_path = "temp.wav"
    audio.export(wav_file_path, format="wav")

    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Load WAV file
    with sr.AudioFile(wav_file_path) as source:
        # Record the audio file as an audio data
        audio_data = recognizer.record(source)

    try:
        # Transcribe audio using Google Speech Recognition
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Error fetching results; {e}"
