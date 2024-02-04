import ffmpeg


def read_video_metadata(video_path):
    try:
        probe = ffmpeg.probe(video_path)
        video_info = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        audio_info = next((stream for stream in probe['streams'] if stream['codec_type'] == 'audio'), None)
        metadata = {
            'video': {
                'codec': video_info['codec_name'],
                'resolution': f"{video_info['width']}x{video_info['height']}",
                'duration': float(video_info['duration']),
            },
            'audio': {
                'codec': audio_info['codec_name'] if audio_info else 'No Audio',
            }
        }
        return metadata
    except ffmpeg.Error as e:
        print(e.stderr)
        raise


# Example usage:
video_path = 'trimmed.mp4'
metadata = read_video_metadata(video_path)
print(metadata)
