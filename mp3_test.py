from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

# Correct the path according to your file location
input_path = r'extracted_audio\Cinnamon Girl.mp3'  # Using a raw string to handle backslashes

try:
    audio = MP3(input_path, ID3=EasyID3)
    print(f"File: {input_path}")
    print("Basic Metadata:")
    for key, value in audio.items():
        print(f"{key}: {value}")
except Exception as e:
    print(f"Error processing the file: {e}")
