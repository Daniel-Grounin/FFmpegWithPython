import ffmpeg

def add_subtitles(video_path, subtitles_path, output_path):
    ffmpeg.input(video_path).output(output_path, vf=f'subtitles={subtitles_path}').run()

# Example usage:
add_subtitles('video.mp4', 'subtitles.srt', 'video_with_subtitles.mp4')
