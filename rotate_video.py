import ffmpeg

def rotate_video(video_path, output_path, rotation_angle):
    if rotation_angle in [90, 270]:
        transpose_code = 2 if rotation_angle == 270 else 1
        vf_filter = f"transpose={transpose_code}"
    elif rotation_angle == 180:
        vf_filter = "transpose=2,transpose=2"
    else:
        raise ValueError("Rotation angle must be 90, 180, or 270 degrees")

    (
        ffmpeg
        .input(video_path)
        .filter_('transpose', vf_filter)
        .output(output_path)
        .run()
    )

# Example usage:
rotate_video('video.mp4', 'video_rotated_90.mp4', 90)
