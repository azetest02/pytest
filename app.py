from flask import Flask
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
        return mymath.add(num1,num2)
