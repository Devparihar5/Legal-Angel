from flask import Blueprint, request, jsonify,current_app
import json
import google.generativeai as genai
from dotenv import load_dotenv
import os
import re

text_app = Blueprint('routes2',__name__)

# Load environment variables
load_dotenv()
api_key = os.getenv('gemini_api_key')
genai.configure(api_key=api_key)

# Main function
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

@text_app.route('/chat-bot', methods=['POST'])
def generate_gemini():
    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "Please provide a prompt"}), 400

    gemini_response = generate_gemini_response(prompt)

    cleaned_text = re.sub(r'\*\*', '', gemini_response)  # Remove double asterisks
    cleaned_text = re.sub(r'\n', ' ', cleaned_text)  # Replace newline characters with space
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()  # Remove extra whitespace and strip leading/trailing spaces

    return jsonify({"Legal_Assistant": cleaned_text})
