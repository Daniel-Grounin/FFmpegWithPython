import ffmpeg

def generate_waveform(input_audio_path, output_image_path):
    (
        ffmpeg
        .input(input_audio_path)
        .filter('showwavespic', s='1024x512')
        .output(output_image_path, vframes=1)
        .run()
    )

# Example usage:
generate_waveform('audio.mp3', 'waveform.png')
