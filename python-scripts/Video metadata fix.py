import subprocess
import os
from generalpy import get_new_path



video_path = 'B:/Desktop/yt-short.mp4'



def run_ffmpeg(input_file):
    _filename = os.path.basename(input_file)
    _dirpath = os.path.dirname(input_file)
    output_file = get_new_path(
        os.path.join(
            _dirpath, 
            f'[FFMPEG] {_filename}'
        )
    )
    print(f'[Data] {input_file=}')
    print(f'[Data] {output_file=}')
    ffmpeg_cmd = f'ffmpeg -i "{input_file}" -map_metadata -1 -c copy "{output_file}"'
    subprocess.run(ffmpeg_cmd, shell=True)


def main():
    input_file = video_path

    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"[Result] Error: Input file '{input_file}' not found.")
        return

    # Run the ffmpeg command
    run_ffmpeg(input_file)
    print("[Result] FFmpeg command executed successfully.")
    





if __name__ == "__main__":
    main()
    print()
