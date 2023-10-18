from flask import Flask, request, send_from_directory, jsonify, render_template
import os
from pytube import YouTube
import subprocess
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

app = Flask(__name__)

def run_demucs(input_file):
    process = subprocess.Popen(['demucs', '-n', 'mdx_extra', input_file], 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.STDOUT, 
                               universal_newlines=True)
    # ... (The rest of your existing code for running demucs)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process_file():
    youtube_url = request.json['youtube_url']
    
    # Download the YouTube video's audio
    yt = YouTube(youtube_url)

    # Get the title of the video
    video_title = yt.title

    video_title = video_title.replace("'", "")
    video_title = video_title.replace("~", "")
    video_title = video_title.replace(":", "")


    video_stream = yt.streams.filter(only_audio=True).first()
    video_stream.download(output_path='downloads')  # Change to your desired path


     # ##################
    # create mp3
    # ##################

    # Replace 'video_path' with the path to your downloaded video file
    #video_path = f'downloads\\{video_title}.mp4'
    video_path = os.path.join('downloads', f'{video_title}.mp4')

    # Replace 'output_audio_path' with the desired path for the audio file
    #output_audio_path = f'extracted_audio\\{video_title}.mp3'
    output_audio_path = os.path.join('extracted_audio', f'{video_title}.mp4')

    # Extract audio from the video
    ffmpeg_extract_audio(video_path, output_audio_path)
    
    # Run demucs on the downloaded file
    # (You'll need to specify the correct file path here)
    #run_demucs('downloads/some_downloaded_file')

    return jsonify(status='File Processed')

@app.route('/download')
def download_file():
    # The filename should be whatever you processed
    return send_from_directory('extracted_audio', 'Latest ChatGPT Update Lets You Do INSANE Things!.mp3')  # Link: https://youtu.be/6bihhz84CTw?si=QjoCxoZujNLnsZno

if __name__ == '__main__':
    app.run(debug=True)
