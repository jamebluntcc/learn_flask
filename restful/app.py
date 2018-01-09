from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class test(Resource):
    def get(self):
        return {'name': 'test'}


api.add_resource(test, '/')

if __name__ == '__main__':
    app.run(debug=True)

