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

@vision_app.route('/vision', methods=['POST'])
def generate():
    try:
        prompt  = """Provide recommendations for relevant IPC (Indian Penal Code) sections based on the given scenario, along with detailed justifications for each suggested section."""

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
                return jsonify({"gemini_output": extracted_text})
            else:
                return jsonify({"error": "Failed to extract text from Gemini response."})

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"})
