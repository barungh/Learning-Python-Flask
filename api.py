from flask import Flask, request
from datetime import datetime 

app = Flask(__name__)


def add(a, b):
    return a + b

@app.route('/')
def home():
    return '<h1>Welcome to the land of Legends of Python</h1>'

@app.route('/api', methods=['GET'])
def api_home():
    return "<h5>API Documentation</h5>"

@app.route('/checktime')
def check_time():
    current_date_time = datetime.now()
    result = current_date_time.strftime("%d-%m-%Y %H:%M:%S")
    return f'Current date and time is {result}'

@app.route('/api/calc', methods=['POST', 'GET'])
def calc():
    a = request.args.get('a', '')
    b = request.args.get('b', '')
    print("Value of a")
    print(a)
    print("Value of b")
    print(b)
    a = int(a)
    b = int(b)
    result = add(a, b)
    print(result)
    return f'<h3>Sum {str(result)}</h3>' 
    

