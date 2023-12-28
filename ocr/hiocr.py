from flask import Flask, request, jsonify
from PIL import Image
import pytesseract as pt
import os

app = Flask(__name__)

pt.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def extract_text_from_image(img_path):
    img = Image.open(img_path)
    text = pt.image_to_string(img, lang="hin")
    return text

@app.route('/extract-text', methods=['POST'])
def extract_text():
    try:
        # Check if the POST request has the file part
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['file']

        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        if file:
            # Save the uploaded file to a temporary folder
            upload_folder = "./temp_images"
            os.makedirs(upload_folder, exist_ok=True)
            img_path = os.path.join(upload_folder, file.filename)
            file.save(img_path)

            # Extract text from the uploaded image
            extracted_text = extract_text_from_image(img_path)

            # Remove the temporary image file
            os.remove(img_path)

            # Return the extracted text in JSON format
            return jsonify({'text': extracted_text})
        
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
