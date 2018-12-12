from bs4 import BeautifulSoup, SoupStrainer
import requests
from .datetotimestamp import cln

datas = []

for i in range(1,4):
    url = 'https://news.kompas.com/search/all/'+str(i)
    r  = requests.get(url)
    
    data = r.text
    only_a_tags = SoupStrainer('div')
    soup = BeautifulSoup(data,"lxml", parse_only=only_a_tags)

    mydivs = soup.findAll('div', class_ = 'article__list clearfix' )
    for t in mydivs:
        datas.append(t)

data_json = []

for i in datas:
    link = i.find('a')['href']
    date = i.find('div', class_='article__date').text
    title = i.find('a', class_='article__link').text
    img = i.find('img')['src']

    data_json.append(
        {
            'link': link,
            'date': cln(date),
            'title': title,
            'img': img,
            'media': 'KOMPAS'
        }
    )