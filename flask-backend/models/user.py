from services.database import db
from datetime import datetime


class ModelUser(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class ModelLoginHistory(db.Model):
    __tablename__ = 'login_history'
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('ModelUser', backref=db.backref('login_history', lazy=True))
