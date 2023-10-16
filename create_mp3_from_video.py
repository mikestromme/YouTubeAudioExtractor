from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

# ##############
# download video
# ##############

# Replace 'video_url' with the URL of the YouTube video you want to download
video_url = 'https://youtu.be/BihcE44msEY?si=QJ431hbf3jjxBNST'

# Create a YouTube object
yt = YouTube(video_url)

# Get the title of the video
video_title = yt.title

video_title = video_title.replace("'", "")

# Choose the stream with audio (usually the first one)
video_stream = yt.streams.filter(only_audio=True).first()

# Download the audio stream
video_stream.download(output_path='downloads')


# ##################
# create mp3
# ##################

# Replace 'video_path' with the path to your downloaded video file
video_path = f'downloads\\{video_title}.mp4'

# Replace 'output_audio_path' with the desired path for the audio file
output_audio_path = f'extracted_audio\\{video_title}.mp3'

# Extract audio from the video
ffmpeg_extract_audio(video_path, output_audio_path)
