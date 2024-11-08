import os
import sys
import argparse
from moviepy.editor import VideoFileClip, AudioFileClip
from denoiser import pretrained
from denoiser.dsp import convert_audio
import torchaudio
import torch


def main():
    parser = argparse.ArgumentParser(description='Denoise audio in a video file')
    parser.add_argument('input', help='Input video file')
    parser.add_argument('output', help='Output video file')
    args = parser.parse_args()

    input_filename = args.input
    denoised_video_filename = args.output
    audio_filename = "audio.wav" 
    denoised_filename = "denoised_audio.wav"

    # Check if files exist
    if not os.path.exists(input_filename):
        print(f"File '{input_filename}' does not exist.")
        sys.exit(1)
        
    # Load video and extract audio
    video = VideoFileClip(input_filename)
    audio = video.audio
    audio.write_audiofile(audio_filename)

    # Clean up
    video.close()
    audio.close()

    # Denoise audio
    model = pretrained.dns64()
    wav, sr = torchaudio.load(audio_filename)
    wav = convert_audio(wav, sr, model.sample_rate, model.chin)
    
    # Process audio through model and save
    with torch.no_grad():
        denoised = model(wav)[0]
    torchaudio.save(denoised_filename, denoised.cpu(), model.sample_rate)

    # Create new video with denoised audio
    video = VideoFileClip(input_filename)
    denoised_audio = AudioFileClip(denoised_filename)
    final_video = video.set_audio(denoised_audio)
    final_video.write_videofile(denoised_video_filename)
    
    # Clean up
    video.close()
    denoised_audio.close()
    final_video.close()


if __name__ == "__main__":
    main()