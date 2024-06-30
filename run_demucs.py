from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import subprocess
from moviepy.editor import *

#import os
#os.environ['PYTHONIOENCODING'] = 'UTF-8'
#sys.setdefaultencoding('utf8')

def run_demucs(input):
    process = subprocess.Popen(['demucs', '--verbose', '-n', 'htdemucs_ft', input], 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.STDOUT, 
                               universal_newlines=True,
                               encoding='utf-8',  # Ensure the subprocess outputs are treated as UTF-8
                               errors='replace')  # Replace characters that cannot be decoded with a placeholder

    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:  # Fix: 'none' should be 'None'
            break  # Exit loop if process is done and no more output
        if output:
            print(output.strip())  # Directly print the decoded line

if __name__ == '__main__':
    
    #input_file = 'extracted_audio\\All of Me.mp3' 
    input_file = 'C:\\Users\\mikes\\Documents\\Development\\Python\\AI\\YouTubeAudioExtractor\\extracted_audio\\I\'ll Stick Around.mp3'

    #byte_string = input
    #decoded_string = byte_string.decode('utf-8')

    # #############
    # create stems
    # #############
    run_demucs(input_file)