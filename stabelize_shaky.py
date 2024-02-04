import ffmpeg

def stabilize_video(input_video_path, output_video_path):
    # Step 1: Analyze the video to detect camera movement
    # This creates a file named 'transforms.trf' used for stabilization
    (
        ffmpeg
        .input(input_video_path)
        .filter('vidstabdetect', result='transforms.trf')
        .output('dummy.mp4', f='null')  # Use a dummy output with null format
        .run(overwrite_output=True)
    )

    # Step 2: Stabilize the video using the transformations data
    (
        ffmpeg
        .input(input_video_path)
        .filter('vidstabtransform', input='transforms.trf', smoothing=5)
        .output(output_video_path)
        .run(overwrite_output=True)
    )

# Example usage
stabilize_video('sliced_video.mp4', 'stabilized_video.mp4')
