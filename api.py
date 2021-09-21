from flask import Flask
from flask import request

app = Flask(__name__)


def add(a, b):
    return a + b

@app.route('/')
def home():
    return 'There is nothing here, <br> contact server admin for API Doc'

@app.route('/api', methods=['GET'])
def api_home():
    return "<h5>API Documentation</h5>"

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
    
