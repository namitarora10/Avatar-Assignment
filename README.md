Object Placement in Text-Conditioned Scenes using Stable Diffusion Inpainting

Table of Contents
Introduction
Features
Examples
Installation
Usage
Generating a Single Image
Generating a Video Sequence
Approach
Results
Experiments
Acknowledgements
Contact
Introduction
Recent advancements in generative AI have revolutionized creative workflows, especially in the realm of realistic product photography. Traditionally confined to studio settings, generating compelling product images for e-commerce can now be achieved through AI techniques. This project focuses on placing an object from a given image into a text-conditioned scene, ensuring that the final output is coherent and natural-looking.

This repository contains executable code that takes an image of an object (with a white background) and a text prompt to generate a scene where the object is placed naturally. Additionally, it provides functionality to create a short video by generating multiple consistent frames, simulating camera movements like zooming or translating.

Features
Text-Conditioned Scene Generation: Place an object into a scene based on a descriptive text prompt.
Stable Diffusion Inpainting: Utilize state-of-the-art inpainting techniques for seamless integration.
Video Generation: Create a sequence of frames to form a video, simulating camera movements or object transitions.
Customization: Modify prompts and parameters to experiment with different scenes and effects.
Examples
Input Image

Generated Image with Prompt: "A pan in a modern kitchen used in meal preparation"

Generated Video (Frames Extract)

Note: The full video can be viewed in the output_video.mp4 file.

Installation
Prerequisites
Python 3.7 or higher
NVIDIA GPU with CUDA support (recommended for faster generation)
Git (to clone the repository)
Steps
Clone the Repository

bash
Copy code
git clone https://github.com/your_username/your_repository.git
cd your_repository
Create a Virtual Environment (Optional but Recommended)

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies

bash
Copy code
pip install --upgrade pip
pip install -r requirements.txt
If requirements.txt is not provided, install the necessary libraries:

bash
Copy code
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install diffusers
pip install transformers
pip install accelerate
pip install pillow
pip install moviepy
Set Up Hugging Face Authentication (If Required)

Some models require authentication to download. Set up Hugging Face CLI:

bash
Copy code
pip install huggingface_hub
huggingface-cli login
Follow the prompts to enter your Hugging Face API token.

Usage
The main script is run.py, which accepts command-line arguments to generate images and videos.

Generating a Single Image
bash
Copy code
python run.py --image ./input_image.png --text-prompt "A pan in a modern kitchen used in meal preparation" --output ./generated_image.png
--image: Path to the input object image.
--text-prompt: Description of the scene to generate.
--output: Path to save the generated image.
Generating a Video Sequence
bash
Copy code
python run.py --image ./input_image.png --text-prompt "A pan in a modern kitchen used in meal preparation" --output ./generated_image.png --video ./output_video.mp4
--video: Path to save the generated video.
Additional parameters like the number of frames and frame duration can be adjusted within the script.

Approach
The core idea is to leverage the Stable Diffusion Inpainting model to integrate an object into a scene based on a text prompt. The process involves:

Loading the Pre-trained Model: Utilizing stabilityai/stable-diffusion-2-inpainting from Hugging Face.
Preparing the Input Image: Ensuring the object image is in the correct format and mode.
Generating the Scene: Feeding the text prompt and object image into the model to generate the composite image.
Video Generation: Creating slight variations in the text prompt or model parameters to produce multiple frames, which are then combined into a video using moviepy.
Results
Through this approach, the object is placed naturally within the scene, aligning with the text prompt while keeping the object's appearance unaltered. The generated images exhibit:

Coherence: The object fits seamlessly into the scene.
Realism: Lighting, shadows, and perspective are adjusted to match the scene.
Alignment with Prompt: The scene reflects the description provided.
Successful Experiments
Pan in a Modern Kitchen: The pan is placed on a stove with appropriate lighting.
Cup on a Wooden Table: The cup appears on a rustic table with natural light.
Failed Experiments
Complex Scenes: Overly detailed prompts sometimes lead to mismatches in object placement.
Multiple Objects: Introducing additional objects in the prompt can confuse the model.
These experiments highlight the importance of prompt engineering and model limitations.

Experiments
Experiment 1: Varying the Text Prompt
Objective: Assess how different prompts affect the placement and appearance of the object.
Method: Used varying descriptions like "A pan in an outdoor camping site" vs. "A pan in a professional chef's kitchen".
Result: The context changes significantly, but the pan remains central and unaltered.
Experiment 2: Generating Camera Movements# Object Placement in Text-Conditioned Scenes using Stable Diffusion Inpainting

![Example Output](./example_output.png)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Examples](#examples)
- [Installation](#installation)
- [Usage](#usage)
  - [Generating a Single Image](#generating-a-single-image)
  - [Generating a Video Sequence](#generating-a-video-sequence)
- [Approach](#approach)
- [Results](#results)
- [Experiments](#experiments)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## Introduction

Recent advancements in generative AI have revolutionized creative workflows, especially in the realm of realistic product photography. Traditionally confined to studio settings, generating compelling product images for e-commerce can now be achieved through AI techniques. This project focuses on placing an object from a given image into a text-conditioned scene, ensuring that the final output is coherent and natural-looking.

This repository contains executable code that takes an image of an object (with a white background) and a text prompt to generate a scene where the object is placed naturally. Additionally, it provides functionality to create a short video by generating multiple consistent frames, simulating camera movements like zooming or translating.

## Features

- **Text-Conditioned Scene Generation**: Place an object into a scene based on a descriptive text prompt.
- **Stable Diffusion Inpainting**: Utilize state-of-the-art inpainting techniques for seamless integration.
- **Video Generation**: Create a sequence of frames to form a video, simulating camera movements or object transitions.
- **Customization**: Modify prompts and parameters to experiment with different scenes and effects.

## Examples

### Input Image

![Input Image](./input_image.png)

### Generated Image with Prompt: "A pan in a modern kitchen used in meal preparation"

![Generated Image](./generated_image.png)

### Generated Video (Frames Extract)

![Frame 1](./frames/frame_1.png)
![Frame 5](./frames/frame_5.png)
![Frame 10](./frames/frame_10.png)

*Note: The full video can be viewed in the `output_video.mp4` file.*

## Installation

### Prerequisites

- Python 3.7 or higher
- NVIDIA GPU with CUDA support (recommended for faster generation)
- Git (to clone the repository)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository

Objective: Create a zoom-out effect in the video.
Method: Modified the prompt incrementally and adjusted model parameters for each frame.
Result: Achieved a smooth transition effect, simulating a camera zooming out.
Acknowledgements
Stable Diffusion: Thanks to Stability AI for providing the pre-trained models.
Hugging Face: For hosting models and providing essential libraries.
OpenAI: For inspiring advancements in generative AI.
Contact
For any questions or clarifications, feel free to reach out:

Email: harsh.maheshwari@avataar.ai
GitHub Issues: Please open an issue in the repository.
This project is open-source and welcomes contributions. If you have ideas for improvements or new features, please consider contributing.
