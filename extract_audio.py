from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

# Replace 'video_path' with the path to your downloaded video file
video_path = 'C:\\Users\\mikes\\Documents\\Development\\Python\\YouTubeAudioExtractor\\downloads\\Vested Interests How a network of billionaires influences AI policy.mp4'

# Replace 'output_audio_path' with the desired path for the audio file
output_audio_path = 'C:\\Users\\mikes\\Documents\\Development\\Python\\YouTubeAudioExtractor\\extracted_audio\\audio.mp3'

# Extract audio from the video
ffmpeg_extract_audio(video_path, output_audio_path)
