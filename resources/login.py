from flask_restful import Resource, reqparse
from models.user import UserModel
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (create_access_token)


class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='You must provide username, none is exist')
    parser.add_argument('password', type=str, required=True, help='You must provide a password, none is exist')

    def post(self):
        data = self.parser.parse_args()

        user = UserModel.find_by_username(data['username'])
        if user and safe_str_cmp(user.password, data['password']):
            access_token = create_access_token(identity=user.username)
            return {
                'status': 'success',
                'code': '200',
                'access_token': access_token,
                'username': user.username
            }, 200
        return {
            'status': 'error',
            'code': '401',
            'message': 'Login Failed, wrong username or password',
        }, 401
