import ffmpeg

def create_video_from_images(image_pattern, output_path, fps=24):
    (
        ffmpeg
        .input(image_pattern, pattern_type='glob', framerate=fps)
        .output(output_path, pix_fmt='yuv420p')
        .run()
    )

# Example usage:
create_video_from_images('images/frame_*.png', 'timelapse.mp4')