from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return '<h1>hello flask</h1>'
