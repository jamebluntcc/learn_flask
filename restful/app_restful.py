import os
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

REST_URL = 'http:0.0.0.0:9000/api/'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'dev.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)

parse = reqparse.RequestParser()
parse.add_argument('admin', type=bool, help='Use super manager mode', default=False)

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'address': fields.String
}

class User(db.Model):
    __tablename__ = 'rest_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    address = db.Column(db.String(128),nullable=True)


db.create_all()

class UserResource(Resource):
    @marshal_with(resource_fields)
    def get(self, name):
        user = User.query.filter_by(name=name).first()
        return user

    def put(self, name):
        address = request.form.get('address', '')
        user = User.query.filter_by(name=name).first()
        if not user:
            user = User(name=name, address=address)
            db.session.add(user)
            db.session.commit()
            return {'ok': 0}, 201
        user.address=address
        db.session.add(user)
        db.session.commit()
        return {'ok': 0}, 201

    def delete(self, name):
        args = parse.parse_args()
        is_admin = args['admin']
        if not is_admin:
            return {'error': 'You do not have permissions'}
        user = User.query.filter_by(name=name).first()
        if not user:
            return {'error': 'not found this name'}
        db.session.delete(user)
        db.session.commit()
        return {'ok': 0}


api.add_resource(UserResource, '/api/users/<name>')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)




