from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import subprocess
#from flask_socketio import SocketIO
import os
import eyed3
from moviepy.editor import *
from tqdm import tqdm
import time

def run_demucs(input):
               
        subprocess.Popen(['demucs', '-n', 'htdemucs_ft', input], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        
   


def getMP3(url,output_folder):
      

    # ##############
    # download video
    # ##############

    # Replace 'video_url' with the URL of the YouTube video you want to download
    video_url = url

    # Create a YouTube object
    yt = YouTube(video_url)

    # Get the title of the video
    video_title = yt.title

    video_title = video_title.replace("'", "")
    video_title = video_title.replace("~", "")
    video_title = video_title.replace(":", "")
    video_title = video_title.replace("/", "")
    video_title = video_title.replace("\"", "")
    video_title = video_title.replace(",", "")
    video_title = video_title.replace("#", "")
    video_title = video_title.replace("?", "")
    #video_title = video_title.replace("-", "")

    # Choose the stream with audio (usually the first one)
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Download the audio stream
    audio_stream.download(output_path='downloads')
    audio_stream.download(filename='temp_audio')    


    # ##################
    # create mp3
    # ##################    

    # Replace 'video_path' with the path to your downloaded video file
    video_path = os.path.join('downloads', f'{video_title}.mp4')

    # Replace 'output_audio_path' with the desired path for the audio file
    output_audio_path = os.path.join(output_folder, f'{video_title}.mp3')


    # Trim the downloaded audio using moviepy
    #audio = audio_stream(output_audio_path)
    #sub_audio = audio.subclip(396)
    #sub_audio.write_audiofile(f"{output_audio_path}.mp3")

    # Extract audio from the video
    ffmpeg_extract_audio(video_path, output_audio_path)

    input = os.path.join(output_folder, f'{video_title}.mp3')   

    # add metadata tags
    audiofile = eyed3.load(input) 
    audiofile.tag.album_artist = "Various"
    audiofile.tag.artist = "Various"
    audiofile.tag.album = "YouTube Rips"
    audiofile.tag.save()


    os.remove(video_path) 

    return input


if __name__ == '__main__':
    # get mp3
    #input = getMP3('https://youtu.be/WDSJobjxuVE?si=ispTJozCHswz6M6P','c:\\Users\\mstromme\Desktop',)

    input = 'c:\\Users\\mstromme\\Desktop\\FUNKY DRUM FILL - Drum Lesson.mp3'

    # #############
    # create stems
    # #############
    run_demucs(input)
    
    
