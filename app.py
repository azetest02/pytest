from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def hello_world():
        return 'Hello, World!!'


@app.route('/name')
def new_world():
        return app.config['APP_NAME']
