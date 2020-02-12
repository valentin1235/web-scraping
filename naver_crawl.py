import urllib.request
import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=python&oquery=%ED%8C%8C%EC%9D%B4%EC%8D%AC&tqi=UC4jcsprvTossThcjQZssssssT0-093442'



html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')




title=[]
linked_url=[]
result=[]

a=soup.find_all(class_="_sp_each_url _sp_each_title")
for i in a:
    title.append(i.attrs['title'])

for i in a:
    linked_url.append(i.attrs['href'])

for i in zip(title,linked_url):
    result.append(
        {
            'title' : i[0],
            'url'   : i[1]
        }
    )

print(result)