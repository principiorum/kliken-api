from bs4 import BeautifulSoup, SoupStrainer
import requests
from .datetotimestamp import cln

datas = []

url = 'https://republika.co.id/index'
r  = requests.get(url)

data = r.text
only_a_tags = SoupStrainer('div')
soup = BeautifulSoup(data,"lxml", parse_only=only_a_tags)

mydivs = soup.findAll('div', class_ = 'set_subkanal' )
for t in mydivs:
    datas.append(t)

data_json = []

for i in datas:
    link = i.find('a')['href']
    date = i.find('h6').text
    title = i.find('a').text
    img = i.find('img')['src']

    data_json.append(
        {
            'link': link,
            'date': cln(date),
            'title': title,
            'img': img,
            'media': 'REPUBLIKA'
        }
    )