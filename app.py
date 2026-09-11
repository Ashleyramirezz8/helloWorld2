from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Ashley Ramirez!'

@app.route('/hello')
def hello_page():
    return 'Hello World from Ashley Ramirez! This is my first HTML page'

if __name__ == '__main__':
    app.run(port=5001)