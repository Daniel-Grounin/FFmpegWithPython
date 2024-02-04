import ffmpeg

def extract_audio_spectrum(input_audio_path, output_image_path):
    (
        ffmpeg
        .input(input_audio_path)
        .filter('showspectrum', mode='combined', size='1024x512', color='intensity')
        .output(output_image_path, vframes=1)
        .run()
    )

# Example usage:
extract_audio_spectrum('audio.mp3', 'spectrum.png')
