from bs4 import BeautifulSoup, SoupStrainer
import requests
from .datetotimestamp import cln

datas = []

for i in range(0,3):
    url = 'https://www.liputan6.com/news/indeks/?page='+str('' if i < 1 else i)
    r  = requests.get(url)
    
    data = r.text
    only_a_tags = SoupStrainer('article')
    soup = BeautifulSoup(data,'lxml',parse_only=only_a_tags)
   
    mydivs = soup.findAll('article', class_ = 'articles--rows--item' )
    
    for t in mydivs:
        datas.append(t)

data_json = []

for i in datas:
    link = i.find('a')['href']
    #date = i.find('time', class_ = )['']
    #date = i.find('span', class_ = 'articles--rows--item__datetime')
    title = i.find('a')['title']
    img = i.find('img')['src']

    data_json.append(
        {
            'link': link,
            #'date': cln(date),
            'title': title,
            'img': img,
            'media': 'LIPUTAN6'
        }
    )