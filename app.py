import os

from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from datetime import timedelta

from resources.filter import Clickbait, NonClickbait
from resources.about import About
from resources.login import Login
from resources.user import UserRegister
from resources.suggestion import Suggestion

app = Flask(__name__)
app.secret_key = 'maimjasjhbfsb345kjb3zhfgnwETert#%@Sf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds=60)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

api = Api(app)


@jwt.expired_token_loader
def my_expired_token_callback():
    return jsonify({
        'status': 'error',
        'code': 401,
        'message': 'The token has expired'
    }), 401


@jwt.unauthorized_loader
def my_unauthorized_loader_callback(callback):
    return jsonify({
        'status': 'error',
        'code': 401,
        'message': 'Please provide active jwt token to get access'
    }), 401


# endpoint list
api.add_resource(Clickbait, '/news/clickbait')
api.add_resource(NonClickbait, '/news/nonclickbait')
api.add_resource(About, '/about')
api.add_resource(Login, '/login')
api.add_resource(UserRegister, '/register')
api.add_resource(Suggestion, '/suggestion')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run()
