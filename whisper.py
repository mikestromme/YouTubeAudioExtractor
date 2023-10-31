import whisper # use pip install openai-whisper

model = whisper.load_model('base.en')
result = model.transcribe("extracted_audio\whisper_example.mp3")

with open("transcription.txt", "w") as f:
    f.write(result["text"])