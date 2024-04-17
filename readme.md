# SD3 Image Generator App

This Streamlit application allows users to generate images using the Stability AI API. It supports both "text-to-image" and "image-to-image" modes, providing a user-friendly interface for creating images based on textual prompts or modifying existing images.

## Features

- **Text-to-Image**: Generate images from textual descriptions.
- **Image-to-Image**: Modify uploaded images based on textual prompts and selected strength settings.

## Installation

To run this application, you will need Python and several dependencies installed.

### Prerequisites

- Python 3.6 or higher
- pip

### Dependencies

Install the required Python packages using:
```
bash
pip install requirements.txt

````
## Usage

To start the application, navigate to the directory containing `app.py` and run the following command:
```
bash
streamlit run app.py
```


The application will start and be accessible through a web browser at `http://localhost:8501`.

## Configuration

Before running the application, ensure you have the necessary API keys from Stability AI. Set these keys in the `headers` dictionary within the `generate_image` function:
```
python
headers = {
"Authorization": "Bearer YOUR_API_KEY",
"Accept": "image/"
}
```

Replace `YOUR_API_KEY` with your actual Stability AI API key.

## Functionality

### Generating Images

1. **Text-to-Image**:
   - Enter a descriptive prompt.
   - Click "Generate Image".
   - View the generated image below the button.

2. **Image-to-Image**:
   - Upload an image.
   - Optionally adjust the strength slider to control the transformation intensity.
   - Enter a prompt describing the desired modifications.
   - Click "Generate Image".
   - View the modified image below the button.

### Output

Generated images are saved in the `./outputs` directory with a timestamp and model prefix, making it easy to keep track of different sessions and models used.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- Stability AI for providing the API used in this application.
- Streamlit for the framework that powers the web interface.

