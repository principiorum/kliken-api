from flask_restful import Resource, reqparse
from crawler import news_crawler_tempo
from crawler import news_crawler_republika
from crawler import news_crawler_kompas
from crawler import news_crawler_viva
from operator import itemgetter
from sklearn.externals import joblib

class Clickbait(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('tmp_code',
		type = str,
		required=True,
		help='This field cannot be left blank'
	)

	def __init__(self):
		self.viva = news_crawler_viva.data_json[:25]
		self.tempo = news_crawler_tempo.data_json[:25]
		self.republika = news_crawler_republika.data_json[:25]
		self.kompas = news_crawler_kompas.data_json[:25]

		self.news_ready = self.tempo+self.republika+self.kompas+self.viva

	def filter(self, data):
	    loaded_model = joblib.load('lsvcmodel.pkl')

	    predicted = loaded_model.predict(data)
	    return predicted

	def get(self):
		data = Clickbait.parser.parse_args()

		if data['tmp_code'] != 'masahmadbagus006':
			return {
				'status': 'success',
				'code': '400',
				'message': 'Unauthorized access'
			}, 400

		t = []
		for i in self.news_ready:
		    t.append(i['title'])

		predicted = self.filter(t)

		news = []
		for x in zip(self.news_ready, predicted):
		    if x[1] == 0:
		        news.append(x[0])

		newlist = sorted(news, key=itemgetter('date'), reverse=True)

		return {
		'status': 'success',
		'code': '200',
		'data': {
				'news': newlist
			}
		}

class NonClickbait(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('tmp_code',
		type = str,
		required=True,
		help='This field cannot be left blank'
	)

	def __init__(self):
		self.viva = news_crawler_viva.data_json[:25]
		self.tempo = news_crawler_tempo.data_json[:25]
		self.republika = news_crawler_republika.data_json[:25]
		self.kompas = news_crawler_kompas.data_json[:25]

		self.news_ready = self.tempo+self.republika+self.kompas+self.viva

	def filter(self, data):
	    loaded_model = joblib.load('lsvcmodel.pkl')

	    predicted = loaded_model.predict(data)
	    return predicted

	def get(self):
		data = Clickbait.parser.parse_args()

		if data['tmp_code'] != 'masahmadbagus006':
			return {
				'status': 'success',
				'code': '400',
				'message': 'Unauthorized access'
			}, 400

		t = []
		for i in self.news_ready:
		    t.append(i['title'])

		predicted = self.filter(t)

		news = []
		for x in zip(self.news_ready, predicted):
		    if x[1] == 1:
		        news.append(x[0])

		newlist = sorted(news, key=itemgetter('date'), reverse=True)

		return {
		'status': 'success',
		'code': '200',
		'data': {
				'news': newlist
			}
		}