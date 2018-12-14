from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    # parser username dan password
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='You must provide username, none is exist')
    parser.add_argument('password', type=str, required=True, help='You must provide a password, none is exist')

    # class method adalah decorator untuk class, intine biar gausah pake nama class
    # jadi pake cls
    @classmethod
    def post(cls):
        data = cls.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {
                'status': 'error',
                'code': '400',
                'message': 'Username already exist'
            }, 400

        user = UserModel(**data)  # data['username'], data['price']
        user.save_to_db()
        return {
            'status': 'success',
            'code': '201',
            'message': 'User created succesfully',
            'data': {
                'username': user.username,
                'x-api-key': user.api_key
            }
        }, 201
