from flask import Blueprint, request, jsonify, current_app
from PyPDF2 import PdfReader
from PIL import Image
import pytesseract as pt
import os
import re
import pickle
import json

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


modelPath = "google/flan-t5-small"

# Create a dictionary with model configuration options, specifying to use the CPU for computations
model_kwargs = {'device':'cpu'}

# Create a dictionary with encoding options, specifically setting 'normalize_embeddings' to False
encode_kwargs = {'normalize_embeddings': False}

# Initialize an instance of HuggingFaceEmbeddings with the specified parameters
embeddings = HuggingFaceEmbeddings(
    model_name=modelPath,     # Provide the pre-trained model's path
    model_kwargs=model_kwargs, # Pass the model configuration options
    encode_kwargs=encode_kwargs # Pass the encoding options
)

class OCRExtractor:
    def __init__(self):
        pt.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    def extract_text_from_image(self, img_path):
        img = Image.open(img_path)
        text = pt.image_to_string(img, lang="hin")
        return text.replace('\n', ' ')

    def extract_text_from_pdf(self, pdf_file):
        text = ""
        pdf_reader = PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text

    def extract_text(self, file_path):
        extracted_text = ""
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            extracted_text = self.extract_text_from_image(file_path)
        elif file_path.lower().endswith('.pdf'):
            with open(file_path, 'rb') as pdf_file:
                extracted_text = self.extract_text_from_pdf(pdf_file)
        return extracted_text.replace('\n', ' ')
    
    def clean_text(self, text):
        cleaned_text = re.sub(r'\{.*?\}', '', text)
        cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
        return cleaned_text

ocr_app = Blueprint('routes1', __name__)
ocr_extractor = OCRExtractor()


# @ocr_app.route('/extract-text', methods=['POST'])
def extract_text():
    try:
        # Check if the POST request has the file part
        if 'file' not in request.files:
            current_app.logger.error('No file part in the request.')
            return jsonify({'error': 'No file part'})

        file = request.files['file']

        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            current_app.logger.error('No selected file.')
            return jsonify({'error': 'No selected file'})

        if file:
            # Save the uploaded file to a temporary folder
            upload_folder = "./temp_files"
            os.makedirs(upload_folder, exist_ok=True)
            file_path = os.path.join(upload_folder, file.filename)
            file.save(file_path)

            # Extract text based on file type (image or pdf)
            extracted_text = ocr_extractor.extract_text(file_path)

            # Remove the temporary file
            os.remove(file_path)

            # Log the successful extraction
            current_app.logger.info('Text extracted successfully.')
            cleaned_text = ocr_extractor.clean_text(extracted_text)

            # Return the extracted text in JSON format
            return str(cleaned_text)

    except Exception as e:
        # Log the exception
        ocr_app.logger.error(f'Error during text extraction: {str(e)}')
        return jsonify({'error': str(e)})

@ocr_app.route('/ipc-sections', methods=['POST'])
def prediction():
    try:
        # Assuming extract_text() returns the FIR details as a string
        fir_details = extract_text()
        print(fir_details)

        # Assuming FAISS.load_local and ipc_model.similarity_search may raise exceptions
        try:
            ipc_model = FAISS.load_local("D:/RJPOLICE_HACK_668_NeuralNomards_4/faiss_index", embeddings)
            predicted_ipc = ipc_model.similarity_search(fir_details, num_results=4)
        except Exception as model_error:
            return jsonify({"error": f"Error loading or using IPC model: {str(model_error)}"}), 500

        output_dict = {}

        # Append each result to the dictionary with the key 'predicted_i'
        for i, result in enumerate(predicted_ipc, start=1):
            key = f"predicted_{i}"
            output_dict[key] = result.page_content

        ipc = json.dumps(output_dict, indent=2)

        return ipc

    except Exception as e:
        # Handle any unexpected exceptions
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500
