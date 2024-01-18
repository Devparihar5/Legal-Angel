# main.py
from flask import Flask
from flask_cors import CORS
from IPC_APP.ocr.ocr import ocr_app as route1
from IPC_APP.gemini.gemini_text import text_app as route2
from IPC_APP.gemini.vision_pro import vision_app as route3
import logging


import warnings

# Apply the filter
warnings.filterwarnings("ignore", category=UserWarning)



app_main = Flask(__name__)

logging.basicConfig(filename='scraper.log',level=logging.DEBUG,format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')

#Allow Cors Origin
CORS(app_main, origins='*', methods=['POST', 'PUT', 'PATCH', 'GET', 'DELETE', 'OPTIONS'],
     expose_headers=['Origin', 'X-Api-Key', 'X-Requested-With', 'Content-Type', 'Accept', 'Authorization','x-csrftoken','dnt','accept-encoding'])

app_main.register_blueprint(route1)
app_main.register_blueprint(route2)
app_main.register_blueprint(route3)

if __name__ == '__main__':
    app_main.run(host='0.0.0.0', debug=True)