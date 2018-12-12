#!flask/bin/python3
import os
from flask import Flask
from flask_restful import Api
from resources.filter import Clickbait, NonClickbait
from resources.about import About

app = Flask(__name__)
app.secret_key = 'maimjasjhbfsb345kjb3zhfgnwETert#%@Sf'

api = Api(app)

api.add_resource(Clickbait, '/news/clickbait')
api.add_resource(NonClickbait, '/news/nonclickbait')
api.add_resource(About, '/about')

if __name__=='__main__':
	#from db import db
	#db.init_app(app)
	app.run()