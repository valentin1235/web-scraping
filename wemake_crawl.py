import requests
from bs4 import BeautifulSoup
req = requests.get('https://front.wemakeprice.com/best')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

url_chunk = soup.select('div.content_main > div > div.box_listwrap > div > a')
img_chunk = soup.select('div.content_main > div > div.box_listwrap > div > a > div > div.item_cont > div.option_txt > p')
price_chunk = soup.select('#_contents > div.content_main > div > div.box_listwrap > div > a > div > div.item_cont > div.option_txt > div > div.price_info > strong > em')

prices = [price_chunk[i].text for i in range(0, len(price_chunk))]
titles = [img_chunk[i].text for i in range(0,len(img_chunk))]
urls = []



for i in range(0, len(url_chunk)):
    a=url_chunk[i]['href']
    scliced_url = a.replace('//front.wemakeprice.com', '')
    urls.append("https://front.wemakeprice.com"+ scliced_url)



wmp_best_info = []
for i in zip(titles,prices,urls):
    wmp_best_info.append(
        {
            'title' : i[0],
            'price' : i[1],
            'urls' : i[2],
        }
    )
    
print(wmp_best_info)
