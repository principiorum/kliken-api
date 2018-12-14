from db import db
import random
import string


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    api_key = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.api_key = self.randString()

    def randString(self):
        oo = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(50))
        return oo

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_key(cls, key):
        return cls.query.filter_by(api_key=key).first()
