from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import subprocess
#from flask_socketio import SocketIO
import os

def getMP3(url):
    # #############
    # create stems
    # #############
    def run_demucs(input):
        process = subprocess.Popen(['demucs', '-n', 'htdemucs_ft', input], 
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

    # Choose the stream with audio (usually the first one)
    video_stream = yt.streams.filter(only_audio=True).first()

    # Download the audio stream
    video_stream.download(output_path='downloads')


    # ##################
    # create mp3
    # ##################

    # video_path = video_path.replace("'", "")
    # video_path = video_path.replace("~", "")
    # video_path = video_path.replace(":", "")
    # video_path = video_path.replace("/", "")
    # video_path = video_path.replace("\"", "")
    # video_path = video_path.replace(",", "")

    # Replace 'video_path' with the path to your downloaded video file
    #video_path = f'downloads\\{video_title}.mp4'
    video_path = os.path.join('downloads', f'{video_title}.mp4')

    # Replace 'output_audio_path' with the desired path for the audio file
    #output_audio_path = f'extracted_audio\\{video_title}.mp3'
    output_audio_path = os.path.join('extracted_audio', f'{video_title}.mp3')

    # Extract audio from the video
    ffmpeg_extract_audio(video_path, output_audio_path)

    # run demucs
    #input =  f'extracted_audio\\{video_title}.mp3'
    input = os.path.join('extracted_audio', f'{video_title}.mp3')
    run_demucs(input)


if __name__ == '__main__':
    # get mp3
    getMP3('https://youtu.be/ToRoOlrn-XY?si=cJlkiPg5dPDBkP5Y')
    
    
