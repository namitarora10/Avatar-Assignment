# Object Placement in Text-Conditioned Scenes using Stable Diffusion Inpainting

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
