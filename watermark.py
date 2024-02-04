import ffmpeg

def apply_watermark(video_path, watermark_path, output_path, position=("main_w-overlay_w-10", "main_h-overlay_h-10")):
    (
        ffmpeg
        .input(video_path)
        .input(watermark_path, filter_='overlay', x=position[0], y=position[1])
        .output(output_path)
        .run()
    )

# Example usage:
apply_watermark('video.mp4', 'watermark.png', 'video_watermarked.mp4')
