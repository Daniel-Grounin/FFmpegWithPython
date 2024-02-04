import ffmpeg

def black_and_white_video(input_video_path, output_video_path):
    (
        ffmpeg
        .input(input_video_path)
        .output(output_video_path, vf="hue=s=0")
        .run()
    )

# Example usage:
black_and_white_video('color_video.mp4', 'bw_video.mp4')
