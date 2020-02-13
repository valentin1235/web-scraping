import requests
from bs4 import BeautifulSoup

url = 'https://velog.io/'
html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')

title_chunk = soup.select('div > div > div > a > h2')
url_chunk = soup.select('div > main > div > div > div > a')

title = [title_chunk[i].text for i in range(0, len(title_chunk))]

url = ['velog.io'+url_chunk[i]['href'] for i in range(0,len(url_chunk))]

result = []

for i in zip(title, url):
    result.append(
        {
            'title' : i[0],
            'url' : i[1]
        }
    )

print(result)