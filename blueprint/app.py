from flask import Flask, redirect, url_for
from blueprint import test
app = Flask(__name__)
app.register_blueprint(test)


@app.route('/')
def index():
    return redirect(url_for('test.page'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)



