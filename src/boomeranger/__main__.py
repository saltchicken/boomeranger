import argparse
import subprocess
import os

def create_boomerang(input_file, output_file):
    command = [
        "ffmpeg", "-i", input_file,
        "-filter_complex", "[0:v]reverse[r];[0:v][r]concat=n=2:v=1[outv]",
        "-map", "[outv]", output_file
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Boomerang video saved as {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Create a boomerang effect from a video file using FFmpeg.")
    parser.add_argument("input", help="Path to the input video file")
    parser.add_argument("output", nargs='?', help="Path to save the output boomerang video file")
    
    args = parser.parse_args()
    
    if not args.output:
        base, ext = os.path.splitext(args.input)
        args.output = f"{base}_boomerang{ext}"
    
    create_boomerang(args.input, args.output)
