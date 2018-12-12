#!flask/bin/python3

from bs4 import BeautifulSoup, SoupStrainer
import requests
from .datetotimestamp import cln

datas = []

url = 'https://www.tempo.co/indeks'
r  = requests.get(url)
        
data = r.text
only_a_tags = SoupStrainer('ul')
soup = BeautifulSoup(data,"lxml", parse_only=only_a_tags)

mydivs = soup.findAll('ul', class_ = 'wrapper')
for t in mydivs:
    datas.append(t)

data_sets = []
for i in datas:
    nox = i.findAll('li')
    for o in nox:
        data_sets.append(o)

data_json = []

for i in data_sets:
    link = i.find('a')['href']
    date = i.find('span').text
    title = i.find('h2').text
    img = i.find('img')['src']

    data_json.append(
        {
            'link': link,
            'date': cln(date),
            'title': title,
            'img': img,
            'media': 'TEMPO'
        }
    )
