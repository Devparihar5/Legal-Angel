### Legal-Angel

#### Project Name: Fir Analysis using AI

**Overview:**
Legal-Angel is a Flask-based web application that provides OCR (Optical Character Recognition) capabilities, text generation using the Gemini AI model, and vision-related functionalities. The application is designed to extract text from images and PDFs, generate legal text using the Gemini AI model, and provide relevant recommendations for Indian Penal Code (IPC) sections based on a given scenario.

#### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Devparihar5/RJPOLICE_HACK_668_NeuralNomards_4.git
   cd RJPOLICE_HACK_668_NeuralNomards_4/backend
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   python main.py
   ```

   The application will be accessible at `http://localhost:5000/`.

#### Project Structure

- `main.py`: Main entry point of the Flask application.
- `IPC_APP/ocr/ocr.py`: OCR-related functionalities and routes.
- `IPC_APP/gemini/gemini_text.py`: Text generation using the Gemini AI model.
- `IPC_APP/gemini/vision_pro.py`: Vision-related functionalities.

#### API Documentation

#### API Documentation

##### 1. **IPC Sections Prediction API**

###### Predict IPC Sections
- **Endpoint:** `/ipc-sections`
- **Method:** POST
- **Request:**
  - Extracted FIR (First Information Report) details.
- **Response:**
  - Predicted IPC sections based on the provided FIR details.

##### 2. **Vision Pro API**

###### Generate Content with Vision
- **Endpoint:** `/vision`
- **Method:** POST
- **Request:**
  - Upload an image file along with a predefined prompt for the Gemini AI model.
- **Response:**
  - Extracted text from the generated content.


##### 3. **Gemini Text Generation API**

###### Generate Legal Text
- **Endpoint:** `/chat-bot`
- **Method:** POST
- **Request:**
  - JSON body with a 'prompt' field containing the input for the Gemini AI model.
- **Response:**
  - Generated legal text based on the provided prompt.

#### Configuration

- **Gemini API Key:**
  - Set your Gemini API key in the environment variable `gemini_api_key`.


#### Demo 
[Click here to watch the demo video](https://github.com/Devparihar5/RJPOLICE_HACK_668_NeuralNomards_4/blob/main/latest-record-video_HwLUAzru.mp4)


#### Sample-Images
![Alt text](https://github.com/Devparihar5/RJPOLICE_HACK_668_NeuralNomards_4/blob/main/BACKEND/demo-images/frontend-demo/image_0.png)
![image-1](https://github.com/Devparihar5/RJPOLICE_HACK_668_NeuralNomards_4/blob/main/BACKEND/demo-images/frontend-demo/image_1.png)
![image-2](https://github.com/Devparihar5/RJPOLICE_HACK_668_NeuralNomards_4/blob/main/BACKEND/demo-images/frontend-demo/image_2.png)
![image-3](https://github.com/Devparihar5/RJPOLICE_HACK_668_NeuralNomards_4/blob/main/BACKEND/demo-images/frontend-demo/image_3.png)
![image-4](https://github.com/Devparihar5/RJPOLICE_HACK_668_NeuralNomards_4/blob/main/BACKEND/demo-images/frontend-demo/image_4.png)


