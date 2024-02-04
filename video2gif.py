import ffmpeg

def video_to_gif(video_path, output_path, start_time, duration):
    (
        ffmpeg
        .input(video_path, ss=start_time, t=duration)
        .output(output_path, vf="fps=10,scale=320:-1:flags=lanczos", loop=0)
        .run()
    )

# Example usage:
video_to_gif('video.mp4', 'clip.gif', start_time='00:00:10', duration=3)
