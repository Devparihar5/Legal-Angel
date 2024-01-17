# main.py
from flask import Flask
from flask_cors import CORS
from IPC_APP.ocr.ocr import ocr_app as route1
import logging


app_main = Flask(__name__)

logging.basicConfig(filename='scraper.log',level=logging.DEBUG,format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')

#Allow Cors Origin
CORS(app_main, origins='*', methods=['POST', 'PUT', 'PATCH', 'GET', 'DELETE', 'OPTIONS'],
     expose_headers=['Origin', 'X-Api-Key', 'X-Requested-With', 'Content-Type', 'Accept', 'Authorization','x-csrftoken','dnt','accept-encoding'])

# Use the Flask Blueprint pattern to mount each app under different routes
app_main.register_blueprint(route1)

if __name__ == '__main__':
    app_main.run(host='0.0.0.0', debug=True)