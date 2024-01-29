# [Lines Calculator](/python-scripts/lines-calculator.py)
  - Calculate number of lines in **all files of a folder**.
  - Files in **sub-folders** will also be analysed.
  - You can also specify the **file types**, like `txt` or `py`.
    - Leave empty to specify all files.

# [Davinci Resolve Video metadata fix](/python-scripts/video-metadata-fix.py)
  - Fixes 'unable to preview' for YT Shorts _([Discussion](https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=165402))_
  - Requirements:
    - FFMPEG must be in the windows 'Path' environment variables
    - Python must be installed
    - Install generalpy library: `pip install generalpy`
  - How to use:
    - Open this `video metadata fix.py` file after downloading and set `video_path` according to your need.
    - Copy this file into your Fusion Scripts directory. _(For windows it is: `C:\Program Files\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Deliver`)_
    - In Davinci Resolve in your render settings (Deliver) use the same File Name for a video as the one you've set in `video_path`, keeping the format. E.g. 'yt-short.mp4', not just 'yt-short'.
    - At the bottom of Deliver settings, enable `Advanced Settings > Trigger script at End of render job`, and choose `video metadata fix` from `script` dropdown.
    - Render your video, a new video will be placed in the same folder as your rendered video.

# [File type finder](/python-scripts/file_type_finder.py)
  - Show a list of all files of specific type *(for ex: .py, .exe etc)*
  - All files from folder and all of its subfolders would be searched
