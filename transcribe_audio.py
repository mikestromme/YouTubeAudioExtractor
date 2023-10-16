import speech_recognition as sr
import subprocess

# Specify the input audio file path (e.g., MP3) and output WAV file path
input_audio_path = 'extracted_audio\\audio.mp3'
output_audio_path = 'extracted_audio\\output.wav'

# FFmpeg command to convert the input audio file to WAV format
ffmpeg_command = [
    'ffmpeg',
    '-i', input_audio_path,
    '-acodec', 'pcm_s16le',  # Set the audio codec to PCM WAV
    '-ar', '16000',          # Set the sample rate to 16000 Hz (optional)
    output_audio_path
]

# Execute the FFmpeg command
try:
    subprocess.run(ffmpeg_command, check=True)
    print("Audio conversion completed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error during audio conversion: {e}")
except FileNotFoundError:
    print("FFmpeg not found. Please ensure it is installed and added to your system's PATH.")




output_audio_path='C:\\Users\\mikes\\Documents\\Development\\Python\\YouTubeAudioExtractor\\extracted_audio\\output.wav'



# Create a recognizer object
recognizer = sr.Recognizer()

# Specify the path to the audio file you want to transcribe (in WAV format)
audio_file_path = output_audio_path

# Load the audio file for transcription
with sr.AudioFile(audio_file_path) as source:
    audio_data = recognizer.record(source)  # Read the entire audio file

# Perform transcription using the CMU Sphinx engine
try:
    transcription = recognizer.recognize_sphinx(audio_data)
    print("Transcription:")
    print(transcription)
except sr.UnknownValueError:
    print("CMU Sphinx could not understand the audio.")
except sr.RequestError as e:
    print(f"Error during recognition with CMU Sphinx: {e}")


