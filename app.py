import streamlit as st
import requests
import datetime
import os
import concurrent.futures
import time

def generate_image(prompt, model, mode, aspect_ratio, output_format, image_path=None, strength=None):
    url = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
    headers = {
        "Authorization": "Bearer YOUR API KEY HERE",
        "Accept": "image/*"
    }
    
    files = {
        "prompt": (None, prompt),
        "model": (None, model),
        "mode": (None, mode),
        "output_format": (None, output_format)
    }
    
    if mode == 'text-to-image':
        files["aspect_ratio"] = (None, aspect_ratio)
    elif mode == 'image-to-image':
        if image_path:
            # Ensure the image is read as binary
            files['image'] = (image_path.name, image_path.getvalue(), 'image/png')
        if strength is not None:
            files['strength'] = (None, str(strength))

    # Log the files dictionary for debugging
    st.write("Sending the following data to the API:")
    st.write(files)

    try:
        response = requests.post(url, headers=headers, files=files)
        response.raise_for_status()  # Will raise an HTTPError for bad requests (4XX or 5XX)
        return response
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to make request: {e}")
        return None

def main():
    st.title("SD3 Image Generator App ⚡️")
    
    prompt = st.text_input("Enter your prompt:")
    mode = st.selectbox("Select the mode:", ["text-to-image", "image-to-image"])
    
    image_file = None
    strength = None
    if mode == 'image-to-image':
        image_file = st.file_uploader("Upload your image:", type=['png', 'jpg', 'jpeg'])
        strength = st.slider("Select strength (0.0 to 1.0):", 0.0, 1.0, 0.5)
    
    aspect_ratio = '1:1'
    output_format = 'png'
    models = ['sd3', 'sd3-turbo']
    
    if st.button("Generate Image"):
        if not prompt:
            st.error("Please enter a prompt.")
        else:
            with st.spinner("Generating images..."):
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    futures = [executor.submit(generate_image, prompt, model, mode, aspect_ratio, output_format, image_file, strength) for model in models]
                    results = [future.result() for future in futures]
                    
                    output_folder = './outputs'
                    if not os.path.exists(output_folder):
                        os.makedirs(output_folder)
                    
                    for result, model in zip(results, models):
                        if result.status_code == 200:
                            current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S").lower()
                            model_prefix = 'sd3' if model == 'sd3' else 'sd3_turbo'
                            output_image_path = f"{output_folder}/{model_prefix}_output_{current_time}.{output_format}"
                            with open(output_image_path, 'wb') as file:
                                file.write(result.content)
                            st.image(output_image_path, caption=f"Generated with {model}")
                        else:
                            st.error(f"Failed to generate with {model}: {result.status_code} - {result.text}")

if __name__ == "__main__":
    main()