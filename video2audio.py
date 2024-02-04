import ffmpeg

def extract_audio_from_video(video_path, audio_path):
    ffmpeg.input(video_path).output(audio_path).run()

# Example usage:
extract_audio_from_video('sliced_video.mp4', 'audio.mp3')
