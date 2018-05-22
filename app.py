from flask import Flask
from flask import request

import mymath

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def hello_world():
        return 'Hello, World'


@app.route('/name')
def new_world():
        return app.config['APP_NAME']


@app.route('/add')
def add_num():
        num1 = request.args.get('num1')
        num2 = request.args.get('num2')
        return str(mymath.add(int(num1),int(num2)))


@app.route('/multiply')
def add_mult():
        num1 = request.args.get('num1')
        num2 = request.args.get('num2')
        return str(mymath.multiply(int(num1),int(num2)))
