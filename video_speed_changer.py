import ffmpeg

def change_video_speed(video_path, output_path, speed_factor):
    if speed_factor > 1:  # Speed up
        filter_ = f"setpts={1/speed_factor}*PTS"
    else:  # Slow down
        filter_ = f"setpts={1/speed_factor}*PTS"
    (
        ffmpeg
        .input(video_path)
        .filter_('setpts', filter_)
        .output(output_path)
        .run()
    )

# Example usage:
change_video_speed('video.mp4', 'video_fast.mp4', speed_factor=2)  # Speed up by 2
change_video_speed('video.mp4', 'video_slow.mp4', speed_factor=0.5)  # Slow down by 2
