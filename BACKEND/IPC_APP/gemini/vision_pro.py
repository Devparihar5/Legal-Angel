from flask import Blueprint, request, jsonify,current_app
import json
import re
import google.generativeai as genai
import re
import os

vision_app = Blueprint("route3",__name__)

from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('gemini_api_key')
genai.configure(api_key=api_key)

def generate_gemini_response(prompt):
    temperature = 0.9
    top_p = 1
    top_k = 1
    max_output_tokens = 2048
    safety_settings = "{}"  


    # Configure the generative model
    generation_config = {
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k,
        "max_output_tokens": max_output_tokens,
    }

    # Set up safety settings (you can modify this part based on your needs)
    safety_settings = json.loads(safety_settings)

    # Create the generative model
    gemini = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings)

    prompt_parts = [prompt]

    try:
        # print(f"Prompt parts: {prompt_parts}")
        response = gemini.generate_content(prompt_parts)
        # print(f"Response text: {response.text}")
        if response.text:
            return response.text
        else:
            return "No output from Gemini."
    except Exception as e:
        return f"An error occurred: {str(e)}"


@vision_app.route('/vision', methods=['POST'])
def generate():
    try:
        # prompt  = """Provide recommendations for relevant IPC (Indian Penal Code) sections based on the given scenario, along with detailed justifications for each suggested section."""
        prompt  = """extract the the data from the given image"""

        if 'image' not in request.files:
            current_app.logger.error('No image part in the request.')
            return jsonify({'error': 'No image part'})

        file = request.files['image']
        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            current_app.logger.error('No selected file.')
            return jsonify({'error': 'No selected file'})
        
        if file:
            upload_folder = "./temp_files"
            os.makedirs(upload_folder, exist_ok=True)
            uploaded_file = os.path.join(upload_folder, file.filename)
            file.save(uploaded_file)

            # Prepare content for Gemini model
            contents = [
                    {
                        "parts": [
                            {
                                "text":prompt
                            },
                            {
                                "image": {
                                    "uploaded_file": uploaded_file
                                }
                            }
                        ]
                    }
                ]

            # Set up the model configuration options
            temperature = 0.9
            top_p = 1
            top_k = 1
            max_output_tokens = 2048


            # Set up the model
            generation_config = {
                "temperature": temperature,
                "top_p": top_p,
                "top_k": top_k,
                "max_output_tokens": max_output_tokens,
            }

            safety_settings = "{}"

            # Check if the query is provided
            if not prompt:
                return jsonify({"error": "Please enter your query."})

            safety_settings = json.loads(safety_settings)
    
            for content in contents:
                for n, part in enumerate(content['parts']):
                    if image := part.get('image', None):
                        if uploaded_file := image.get('uploaded_file', None):
                            with open(uploaded_file, 'rb') as file:
                                data = file.read()
                            mime_type = image.get('mime_type', 'image/png')

                        else:
                            return jsonify({"error": 'Either uploaded_file or image_url must be provided.'})

                        if mime_type is None:
                            mime_type = 'image/png'

                        blob = {'data': data, 'mime_type': mime_type}
                        content['parts'][n] = blob

            gemini = genai.GenerativeModel(model_name='gemini-pro-vision')

            response = gemini.generate_content(
                contents,
                generation_config=generation_config,
                safety_settings=safety_settings,
                stream=False
            )

            data_str = str(response.candidates[0])

            # Use regular expressions to extract the text part
            match = re.search(r'text: "(.*?)"', data_str)

            if match:
                extracted_text = match.group(1)
                cleaned_text = re.sub(r'\*\*', '', extracted_text)  # Remove double asterisks
                cleaned_text = re.sub(r'\n', ' ', cleaned_text)  # Replace newline characters with space
                cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()  # Remove extra whitespace and strip leading/trailing spaces
                # print(cleaned_text)
                
                prompt = f"""suggest the applicable ipc section for the given schenario {cleaned_text}"""
                gemini_response = generate_gemini_response(prompt)

                cleaned_text = re.sub(r'\*\*', '', gemini_response)  # Remove double asterisks
                cleaned_text = re.sub(r'\n', ' ', cleaned_text)  # Replace newline characters with space
                cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()  # Remove extra whitespace and strip leading/trailing spaces
                print(cleaned_text)

                return jsonify({"gemini_output": cleaned_text})
            else:
                return jsonify({"error": "Failed to extract text from Gemini response."})

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"})
