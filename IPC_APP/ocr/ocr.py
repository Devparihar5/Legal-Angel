from flask import Blueprint, request, jsonify, current_app
from PyPDF2 import PdfReader
from PIL import Image
import pytesseract as pt
import os

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

ocr_app = Blueprint('routes1', __name__)
ocr_extractor = OCRExtractor()


@ocr_app.route('/extract-text', methods=['POST'])
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

            # Return the extracted text in JSON format
            return jsonify({'text': extracted_text})

    except Exception as e:
        # Log the exception
        ocr_app.logger.error(f'Error during text extraction: {str(e)}')
        return jsonify({'error': str(e)})
