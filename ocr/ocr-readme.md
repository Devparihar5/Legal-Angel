# OCR-Hindi

## Overview

This Flask application provides a simple API for extracting text from uploaded images. Users can submit an image file using a `POST` request to the `/extract-text` endpoint, and the API will return the extracted text in JSON format.

## Setup

### Prerequisites

- Python 3.x
- Flask (`pip install Flask`)
- Tesseract OCR (install Tesseract and set the correct path in the script)
    - https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Devparihar5/RJPOLICE_HACK_668_NeuralNomards_4.git
   cd RJPOLICE_HACK_668_NeuralNomards_4
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server:

   ```bash
   cd ocr
   python hiocr.py
   ```

2. Open Postman and create a new request.

3. Set the request type to `POST` and enter the following URL:

   ```
   http://127.0.0.1:5000/extract-text
   ```

4. Switch to the "Body" tab, select the "form-data" option, and add a key-value pair with the key `file` and the value as the image file you want to upload.

5. Click the "Send" button to submit the request.

6. View the response in JSON format, containing the extracted text from the uploaded image.

## API Endpoint

### `POST /extract-text`

- **Description:** Extracts text from the uploaded image.
- **Request Type:** `POST`
- **Request Body:** Form-data with key `file` and the value as the image file.
- **Response Format:** JSON
- **Response Example:**
  ```json
  {
    "text": "The extracted text from the image."
  }
  ```