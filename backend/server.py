# Import flask and datetime
from flask import Flask
import datetime
 
x = datetime.datetime.now()
 
# Initializing flask app
app = Flask(__name__, static_folder='../build', static_url_path='/')

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


@app.route('/')
def index():
    return app.send_static_file('index.html')
 
 
# data: name and date
@app.route('/data')
def get_time():
    return {
        'Name':"alpha beta", 
        "Date":x, 
        }
 
     
# Running app
if __name__ == '__main__':
    app.run(debug=True, port=5001)