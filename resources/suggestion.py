from flask_restful import Resource, reqparse
from models.suggestion import SuggestionModel
from flask_jwt_extended import jwt_required


class Suggestion(Resource):
    # parser username dan password
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='You must provide username, none is exist')
    parser.add_argument('news_title', type=str, required=True, help='You must provide a news title, none is exist')
    parser.add_argument('news_link', type=str, required=True, help='You must provide news link, none is exist')
    parser.add_argument('value', type=str, required=True, help='You must provide a suggestion, none is exist')

    # class method adalah decorator untuk class, intine biar gausah pake nama class
    # jadi pake cls
    @classmethod
    @jwt_required
    def post(cls):
        data = cls.parser.parse_args()

        # prepare duplicate news title prevention later
        if SuggestionModel.find_by_title(data['news_title']):
            return {
                'status': 'success',
                'code': '201',
                'message': 'Suggestion saved succesfully'
            }, 201

        suggestion = SuggestionModel(**data)
        suggestion.save_to_db()
        return {
            'status': 'success',
            'code': '201',
            'message': 'Suggestion saved succesfully',
        }, 201
