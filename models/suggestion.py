from db import db


class SuggestionModel(db.Model):
    __tablename__ = 'suggestion'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    news_title = db.Column(db.Text())
    news_link = db.Column(db.Text())
    value = db.Column(db.String(30))

    def __init__(self, username, news_title, news_link, value):
        self.username = username
        self.news_title = news_title
        self.news_link = news_link
        self.value = value

    def json(self):
        return {
            'username': self.username,
            'news_title': self.news_title,
            'news_link': self.news_link,
            'value': self.value
        }

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(news_title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
