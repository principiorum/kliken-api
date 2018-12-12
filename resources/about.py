from flask_restful import Resource

class About(Resource):
	def get(self):
		b = {
	'nama_apl': 'Kliken',
	'versi': '1.0',
	'license': 'MIT',
	'description': 'Aplikasi untuk menghilangkan berita clickbait yang ada di portal berita indonesia',
	'creator': ['Sivi Almanaf Ali Shahab','Muhammad Salma Abdul Aziz', 'Rauzan Sumara','Bagas Alfiandhi Nugroho','Thomi Dhia']
	}
		return {
		'status': 'success',
		'code': '200',
		'data': b
		}