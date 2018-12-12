from bs4 import BeautifulSoup, SoupStrainer
import requests
from .datetotimestamp import cln

datas = []
mo = []

url = 'https://www.viva.co.id/indeks/all/all/'
r  = requests.get(url)

data = r.text
only_a_tags = SoupStrainer('div')
soup = BeautifulSoup(data,"lxml", parse_only=only_a_tags)

mydivs = soup.findAll('div', class_ = 'content_center' )
aaa = soup.findAll('div', class_ = 'thumb' )

for t in zip(mydivs,aaa):
    datas.append(t)


data_json = []

for a in datas:
    i = list(a)
    link = i[0].find('a', class_= 'title-content')['href']
    date = i[0].find('div',class_='date').text
    title = i[0].find('h3').text
    img = i[1].find('img')['data-original']

    data_json.append(
        {
            'link': link,
            'date': cln(date),
            'title': title,
            'img': img,
            'media': 'VIVA'
        }
    )