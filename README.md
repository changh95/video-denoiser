# Video denoiser

Simple python script to denoise audio within a video file.

## Usage

Probably can run on laptop CPUs.

```
# Install dependencies
pip3 install -r requirements.txt

# Run script
python main.py <input_video.mp4> <output_video.mp4>
```

## Notes

If you have some important background music, it will be removed.

Original audio track will be saved as 'audio.wav', so you can use it on a video editor like Davinci Resolve or Final Cut Pro, to overdub the music-only part.

Consider using this script to remove white noise in a speech video.