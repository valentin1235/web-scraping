import requests
from bs4 import BeautifulSoup

url = 'https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=django&l=%EC%84%9C%EC%9A%B8+%EA%B0%95%EB%82%A8%EA%B5%AC'


html = requests.get(url).text

soup = BeautifulSoup(html,'html.parser')

#titles_all = soup.find_all(class_="jobtitle turnstileLink") #- find_all로 불러와서 최하위태그에서 class_= 값불러오기
#print(titles_all[0].attrs['href']) - find_all로 불러와도 최말단태그면이고 그태그 안에 href있으니깐 사용가능
titles= soup.select('div.title > a') #div 태그 안의 a태그를 다불러오는거임. a태그도 클래스가 있지만 a.jobtitle turnstileLink  형태로 클래스를 넣어주면 결과가 빈리스트가 리턴되니 a태그 까지만 달아주기.
locations= soup.select('div.sjcl > span')


#print(titles_all)
#print(titles)

#print(titles[0].a['href']) # 위에서 titles가 a태그를 끝값으로 불러왔으니깐 a['href]를 속성으로 사용불가
                            # .a빼고 ['href']까지만 넣으면 원하는 url 뽑을 수 있음
'''
url=[titles[i].a['href'] for i in range(0,len(titles))]
title=[titles[i].text for i in range(0,len(titles))]
location = [locations[i].text for i in range(0, len(locations))]


job_info=[]
for i in zip(url, title, location):
    job_info.append(
        {
            'url' : i[0],
            'title' : i[1],
            'location' : i[2],
        }
    )

print(job_info)




'''