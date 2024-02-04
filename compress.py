import ffmpeg

def compress_video(input_video_path, output_video_path, video_bitrate="800k"):
    (
        ffmpeg
        .input(input_video_path)
        .output(output_video_path, video_bitrate=video_bitrate)
        .run()
    )

# Example usage:
compress_video('video.mp4', 'compressed.mp4')
