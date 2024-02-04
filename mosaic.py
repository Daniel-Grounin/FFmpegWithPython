import ffmpeg


def create_video_mosaic(main_video_path, pip_video_path, output_path, pip_size=(320, 240), pip_position=("10", "10")):
    main_input = ffmpeg.input(main_video_path)
    pip_input = ffmpeg.input(pip_video_path).filter_('scale', pip_size[0], pip_size[1])

    (
        ffmpeg
        .filter_([main_input, pip_input], 'overlay', x=pip_position[0], y=pip_position[1])
        .output(output_path)
        .run()
    )


# Example usage:
create_video_mosaic('input.mp4', 'video.mp4', 'video_mosaic.mp4')
