from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Lift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lift_name = db.Column(db.String(25))
    weight = db.Column(db.Float)
    reps = db.Column(db.Integer)
    max = db.Column(db.Float, default=0)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<{}: est 1RM {}>'.format(self.lift, self.max)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))