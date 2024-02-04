import ffmpeg


def convert_video_format(input_video_path, output_video_path):
    ffmpeg.input(input_video_path).output(output_video_path).run()


def extract_audio_from_video(video_path, audio_path):
    ffmpeg.input(video_path).output(audio_path).run()


def slice_video(video_path, start_time, duration, output_path):
    (
        ffmpeg
        .input(video_path, ss=start_time, t=duration)
        .output(output_path)
        .run()
    )

def merge_audio_video(audio_path, video_path, output_path):
    ffmpeg.concat(
        ffmpeg.input(video_path).video,
        ffmpeg.input(audio_path).audio,
        v=1, a=1
    ).output(output_path).run()


def main():
    convert_video_format('video.mp4', 'output.avi')

    extract_audio_from_video('trimmed.mp4', 'audio.mp3')

    slice_video('input.mp4', start_time='00:00:10', duration=5, output_path='trimmed.mp4')

    # convert with custom audio codec
    ffmpeg.input("input.mp4").output('custom_audio_codec.mp3', acodec='libshine').run()

    # extract frames from video
    ffmpeg.input("input.mp4").output('frame_%d.png', vframes=3).run()

    # extract audio from video
    ffmpeg.input("input.mp4").output('frame%d.png', vf='fps=1').run()

    # #extract audio from video
    ffmpeg.input("input.mp4", ss="00:00:15").output("thumbnail.png", vframes=1).run()

    merge_audio_video('audio.mp3', 'video.mp4', 'final.mp4')


if __name__ == "__main__":
    main()
