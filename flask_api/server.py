# Imports
from flask import Flask
import os
import datetime
 
x = datetime.datetime.now()
 
# Get Environment Varialbles
FLASK_ENV = os.environ.get('FLASK_ENV')
FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')

# Initializing flask app ...
    
if FLASK_ENV == "production":
    app = Flask(__name__, static_folder='../build', static_url_path='/') # production 
else:
    app = Flask(__name__)  # development

 # Routes   
@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

@app.route('/')
def index():
    return app.send_static_file('index.html')
 
# data: name and date
@app.route('/api/data')
def get_time():
    return {
        'Name':"alpha", 
        "Date":x, 
        "Environment": FLASK_ENV,
        "Port": FLASK_RUN_PORT
        }
 
# Running app
if __name__ == '__main__':
    app.run(debug=True, port=FLASK_RUN_PORT)