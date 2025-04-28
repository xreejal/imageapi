# Multi-Image Composite Generator

## Project Overview
This tool accepts 3–5 reference images along with a user-provided instruction prompt. It generates a new composite image by blending the described visual elements using OpenAI's DALL-E 3 API. The final output is saved in PNG format and also returned as a Base64-encoded string.

## Features
- Supports 3–5 input images (URLs or local paths).
- Preprocesses images (resize to 1024x1024 and convert to RGB).
- Constructs detailed prompts for image generation.
- Saves the generated image locally and encodes it in Base64.
- Error handling for API issues and missing files.

## Setup Instructions
1. Clone the repository or download the project files.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
4. Run the script:
   ```bash
   python scraper.py
   ```

## Output
- Generated images are saved in the `output/` directory.
- The script prints both the output path and a snippet of the Base64-encoded image string.

## Requirements
- Python 3.9+
- OpenAI Python SDK >= 1.11.1
- Pillow >= 10.0.0
- Requests >= 2.31.0
- Python-dotenv >= 1.0.1

## Notes
- This solution uses OpenAI’s DALL-E 3 API, which only supports text-based prompts and does not accept raw images as inputs.
- API keys should be kept secure and are not committed into the codebase.
