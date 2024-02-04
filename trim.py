import ffmpeg

def slice_video(video_path, start_time, duration, output_path):
    (
        ffmpeg
        .input(video_path, ss=start_time, t=duration)
        .output(output_path)
        .run()
    )

# Example usage:
slice_video('input.mp4', start_time='00:00:10', duration=5, output_path='sliced_video.mp4')
