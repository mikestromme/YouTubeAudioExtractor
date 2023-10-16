from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import subprocess
#from flask_socketio import SocketIO


# #############
# create stems
# #############
def run_demucs(input):
    process = subprocess.Popen(['demucs', '-n', 'mdx_extra', input], 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.STDOUT, 
                               universal_newlines=True)

    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            # parse the output to get progress information
            # send progress back to the browser
            print(output.strip())  # for testing, you can print it out
            #socketio.emit('update_progress', {'progress': progress})

# ##############
# download video
# ##############

# Replace 'video_url' with the URL of the YouTube video you want to download
video_url = 'https://youtu.be/mnce5gS8vfY?si=OFkS4DnsBP5h00kl'

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

# run demucs
input =  f'extracted_audio\\{video_title}.mp3'
run_demucs(input)
