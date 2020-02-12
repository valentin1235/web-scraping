import requests
from bs4 import BeautifulSoup
req = requests.get('https://www.billboard.com/charts/hot-100')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

rank = soup.select('li > button > span.chart-element__rank.flex--column.flex--xy-center.flex--no-shrink > span.chart-element__rank__number')

title = soup.select('li> button > span.chart-element__information > span.chart-element__information__song.text--truncate.color--primary')

name = soup.select('li > button > span.chart-element__information > span.chart-element__information__artist.text--truncate.color--secondary')



result=[]
for i in zip(rank, title, name):

    result.append(
        {
            'rank'  : i[0].text,
            'title' : i[1].text,
            'name'  : i[2].text,
        }
    )
    print(result)
    