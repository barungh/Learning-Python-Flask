from flask import Flask, request
from datetime import datetime # this is required to show date and time

app = Flask(__name__)

def peri(l, b):
    perimeter = 2*(l+b)
    return perimeter

@app.route('/')
def hello():
    return '<h1>Welcome to the land of Legends of Python</h1>'

# this is 'localhost/about' route
@app.route('/about')
def greet():
    return f'We are legend of Python'

# and this , 'localhost/checktime' route
@app.route('/checktime')
def check_time():
    current_date_time = datetime.now()
    result = current_date_time.strftime("%d-%m-%Y %H:%M:%S")
    return f'Current date and time is {result}'

@app.route('/calc', methods=['POST', 'GET'])
def calc():
    a = request.args.get('a', '')
    b = request.args.get('b', '')
    a = int(a)
    b = int(b)
    result = peri(a, b)
    result = str(result)
    return result
