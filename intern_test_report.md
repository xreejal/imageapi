# Intern Technical Test Report

## Project: Multi-Image Generation using OpenAI API

### Objective
Develop a tool that accepts 3–5 reference images and a text instruction, then generates a single coherent composite image using a GPT-based image generation API.

### Approach
- Downloaded and preprocessed input images (resized to 1024x1024 pixels, RGB format).
- Built a detailed instruction prompt for DALL-E 3.
- Used the OpenAI DALL-E 3 API to generate a final image based on the prompt.
- Output the image in PNG format and returned both the file path and Base64 encoding for verification.

### Libraries Used
- openai (v1.11.1)
- python-dotenv (v1.0.1)
- pillow (v10.0.0)
- requests (v2.31.0)

### Test Cases

#### Test Case 1: Cinematic Animal Fantasy
- **Reference Images**: Cats and dogs with fantasy-like sunset backgrounds
- **Prompt**: Blend the animals into a dramatic fantasy landscape under a vivid sunset sky.
- **Result**: Successfully generated a vivid, colorful landscape combining animals and beach elements naturally.

#### Test Case 2: Style Transfer Test
- **Reference Images**: Painting style + subject photo + sunset background
- **Prompt**: Render the subject in the painting style of the first image with a sunset background.
- **Result**: Style applied successfully; colors and brushstroke textures merged naturally.

#### Test Case 3: Object Insertion
- **Reference Images**: Street background + bicycle image
- **Prompt**: Insert the bicycle naturally into the street scene matching perspective and shadows.
- **Result**: Bicycle integrated seamlessly into the street setting, matching scale and lighting.

### Notes
- DALL-E 3 API does **not** accept direct image inputs; the solution uses descriptive prompts.
- Secure API key handling and error logging are implemented.
- Output is stored in a separate folder in PNG format.

---
