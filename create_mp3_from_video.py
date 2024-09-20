from yt_dlp import YoutubeDL
from yt_dlp.postprocessor.common import PostProcessor
import os
from run_demucs import run_demucs 

def clean_filename(filename):
    chars_to_replace = ['@', ':', ',', '~', '#', '?', "'", '"', '|', '/', '⧸']
    for char in chars_to_replace:
        filename = filename.replace(char, ' ')
    return filename.strip()

class FileNameCleanerPP(PostProcessor):
    def run(self, info):
        filename = info['filepath']
        cleaned_filename = clean_filename(filename)
        if filename != cleaned_filename:
            if not os.path.exists(cleaned_filename):
                os.rename(filename, cleaned_filename)
                info['filepath'] = cleaned_filename
            else:
                self.to_screen(f'File {cleaned_filename} already exists. Skipping rename.')
        return [], info

def getMP3(url, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'keepvideo': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        video_title = clean_filename(info['title'])
        final_filename = os.path.join(output_folder, f'{video_title}.mp3')

        if os.path.exists(final_filename):
            print(f"File {final_filename} already exists. Skipping download.")
            return final_filename

        ydl.download([url])

    # Delete the webm file
    webm_filename = os.path.join(output_folder, f"{video_title}.webm")
    if os.path.exists(webm_filename):
        try:
            os.remove(webm_filename)
            print(f"Deleted webm file: {webm_filename}")
        except Exception as e:
            print(f"Error deleting webm file: {e}")

    return final_filename

if __name__ == '__main__':
    # get mp3
    output_path = r'C:\Users\mikes\Documents\Development\AI\YouTubeAudioExtractor\separated\htdemucs_ft\Input'
    #input = getMP3('https://youtu.be/PjjNvjURS-s?si=7ypaDD90NpkOfI1r', 'downloads')  # rush song - has odd character in title - fixed
    input = getMP3('https://youtu.be/eb3kAUQxinQ?si=oyyoprExg0uIsaM1', output_path)
    print(f"Downloaded or found file: {input}")

       
    # #############
    # create stems
    # #############
    run_demucs(input)