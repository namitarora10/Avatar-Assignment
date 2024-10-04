import argparse
from PIL import Image
import torch
from diffusers import StableDiffusionInpaintPipeline
import moviepy.editor as mpy
import os

# Load the model (stable-diffusion-inpainting)
def load_model():
    print("Loading model...")
    model_id = "stabilityai/stable-diffusion-2-inpainting"
    
    try:
        # Enable low memory mode if possible
        pipe = StableDiffusionInpaintPipeline.from_pretrained(model_id, torch_dtype=torch.float16, low_cpu_mem_usage=True)
        pipe = pipe.to("cuda")  # Assuming GPU available, you can modify this to "cpu" if no GPU
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")
        raise

    return pipe

# Function to generate an image based on a prompt
def generate_image(pipe, image_path, text_prompt, output_path):
    # Load the object image
    print("Loading input image...")
    try:
        image = Image.open(image_path).convert("RGB")
        print(f"Image loaded: {image.size}, {image.mode}")
    except Exception as e:
        print(f"Error loading image: {e}")
        return

    # Set up the text prompt
    print(f"Generating image with prompt: {text_prompt}")
    try:
        result = pipe(prompt=text_prompt, image=image).images[0]
        print("Image generated, saving to output path.")
        result.save(output_path)
        print(f"Generated image saved to {output_path}")
    except Exception as e:
        print(f"Error generating or saving image: {e}")
        return

# Function to generate multiple frames for video creation
def generate_frames(pipe, image_path, text_prompt, output_dir, num_frames=10):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    frames = []
    for i in range(num_frames):
        # Slight variation to simulate movement (e.g., camera zoom or translation)
        modified_prompt = f"{text_prompt} (Frame {i+1})"
        output_frame = os.path.join(output_dir, f"frame_{i+1}.png")
        print(f"Generating frame {i+1}")
        generate_image(pipe, image_path, modified_prompt, output_frame)
        frames.append(output_frame)
    return frames

# Function to combine frames into a video
def create_video(frames, video_output):
    print("Creating video from frames...")
    clips = [mpy.ImageClip(f).set_duration(0.5) for f in frames]
    video = mpy.concatenate_videoclips(clips, method="compose")
    video.write_videofile(video_output, fps=24)
    print(f"Video saved to {video_output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate text-conditioned images and videos using Stable Diffusion Inpainting")
    parser.add_argument("--image", type=str, required=True, help="Path to the input image")
    parser.add_argument("--text-prompt", type=str, required=True, help="Text prompt for the scene generation")
    parser.add_argument("--output", type=str, required=True, help="Path to save the generated image")
    parser.add_argument("--video", type=str, required=False, help="Path to save the generated video (optional)")

    args = parser.parse_args()

    # Load the model
    try:
        pipe = load_model()
    except Exception as e:
        print(f"Failed to load model: {e}")
        exit()

    # Generate a single image
    try:
        generate_image(pipe, args.image, args.text_prompt, args.output)
    except Exception as e:
        print(f"Failed to generate image: {e}")
        exit()

    # If video path is provided, generate frames and create a video
    if args.video:
        try:
            frame_dir = "frames"
            frames = generate_frames(pipe, args.image, args.text_prompt, frame_dir, num_frames=10)
            create_video(frames, args.video)
        except Exception as e:
            print(f"Failed to generate video: {e}")
            exit()
