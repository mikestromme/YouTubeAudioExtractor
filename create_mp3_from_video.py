from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import os
import eyed3
from moviepy.editor import *
from run_demucs import run_demucs 
   


def getMP3(url,output_folder):
      

    # ##############
    # download video
    # ##############

    # Replace 'video_url' with the URL of the YouTube video you want to download
    video_url = url

    # Create a YouTube object
    yt = YouTube(video_url)

    #replace characters from yt title
    yt.title = yt.title.replace("@","")
    yt.title = yt.title.replace(":","")
    yt.title = yt.title.replace(",","")
    yt.title = yt.title.replace(".","")
    yt.title = yt.title.replace(" ","_")
    yt.title = yt.title.replace("~","")
    yt.title = yt.title.replace("#","")
    yt.title = yt.title.replace("?","")
    yt.title = yt.title.replace("'","")
    yt.title = yt.title.replace('"',"")
    yt.title = yt.title.replace('|',"")

    # Get the title of the video
    video_title = yt.title    

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
    input = getMP3('https://youtu.be/N4F2weWYLlM?si=RCiNNBIdwZA-s0hd','extracted_audio')

    # #############
    # create stems
    # #############
    #run_demucs(input)
    
    
