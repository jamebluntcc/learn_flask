from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
Column = db.Column


class User(db.Model):
    __tablename__ = 'user'
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(128))
    password_hash = Column(db.String(128))

    def __init__(self, name, password):
        self.name = name
        self.password_hash = generate_password_hash(password)

    @property
    def password(self):
        raise AttributeError('password not readable!')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)




