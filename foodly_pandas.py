import requests, csv, re
from bs4 import BeautifulSoup
import pandas as pd

# empty list set to add new column
mCols = []
df = pd.DataFrame(columns=mCols)

# space deleteing function
def re_palce(tag):
    pattern  = re.compile(r'\s+')
    sentence = re.sub(pattern, ' ', tag)
    return sentence

# set empty list waiting for appending
descs          = []
prices         = []
titles         = []
small_imgs     = []
big_imgs       = []
harvest_year   = []
is_in_stock    = []
measures       = []
vitamins       = []
minerals       = []
energys        = []
carbonhydrates = []
fats           = []
proteins       = []

# access from first page to last page
last_page = 6
for i in range(1,last_page):
    url = f'https://foodly-store.myshopify.com/collections/all-products?page={i}'

    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    a=soup.select('div.product__visuals > a')
    b=soup.select('div.product__visuals > a > div >img')
    c=soup.select('div.product__info > span')

# get product details(harvest_years, measures, is_in_stock)
    for i in range(0,len(c)):
# unnecessary indent remover
        sense = re_palce(c[i].text).split('|')
        
        if sense is not None:
            harvest_year.append(sense[0])
            is_in_stock.append(sense[1])
            measures.append(sense[-1])
        else:
            harvest_year.append('')
            is_in_stock.append('')
            measures.append('')
        

# get image url
    for i in range(0,len(b)):
        small_imgs.append('https:' + b[i]['src'])

# get title
    for i in range(0,len(a)):
        titles.append(a[i]['title'])


# get prodcut deatail page url
    d = soup.select('div.product__info > h4 > a')
    unit_urls = ['https://foodly-store.myshopify.com'+d[i]['href'] for i in range(len(d))]
# access to each and every product detail page 
    for i in unit_urls:
        html = requests.get(i).text
        soup = BeautifulSoup(html, 'html.parser')
        
        desc   = soup.select('div.product__desc')
        price  = soup.select('span.js-price-and-value > span.money')
        sense2 = re_palce(desc[0].text)
        descs.append(sense2)
        prices.append(price[0].text)


# get energy info
        try:
            energy = soup.select_one('li > span > strong')
            energys.append(energy.text)
        except:
            energy = ''
            energys.append(energy)

# get carbonhydrate info
        try:
            carbonhydrate = soup.select('li:nth-child(2) > span > strong')
            carbonhydrates.append((carbonhydrate[0].text))
        except :
            carbonhydrate = ''
            carbonhydrates.append(carbonhydrate)

# get fat info
        try:
            fat = soup.select('li:nth-child(3) > span > strong')
            fats.append((fat[0].text))
        except :
            fat = ''
            fats.append(fat)

# get protein info
        try:
            protein = soup.select('li:nth-child(4) > span > strong')
            proteins.append((protein[0].text))
        except :
            protein = ''
            proteins.append(protein)

# get big_image(background image) url            
        try:
            big_img = soup.select('ul.slides > li > img')
            big_imgs.append('https'+big_img[0]['src'])
        except:
            big_img = ''
            big_imgs.append(big_img)
        
# get vitamin info
        try:
            vitamin = soup.select_one('#container > div.parallax__base > div:nth-child(4) > div > div > div > div > div:nth-child(2) > ul').text
            vitamin_sense = re_palce(vitamin)
            vitamins.append(vitamin_sense)
        except :
            vitamin =''
            vitamins.append(vitamin)

# get mineral info
        try:
            mineral = soup.select_one('#container > div.parallax__base > div:nth-child(4) > div > div > div > div > div:nth-child(3) > ul').text
            mineral_sense = re_palce(mineral)
            minerals.append(mineral_sense)
        except :
            mineral = ''
            minerals.append(mineral)

# put values in each list to created column to data frame
df['titles']         = titles
df['prices']         = prices
df['descs']          = descs
df['small_imgs']     = small_imgs
df['big_imgs']       = big_imgs
df['energys']        = energys
df['carbonhydrates'] = carbonhydrates
df['proteins']       = proteins
df['fats']           = fats
df['minerals']       = minerals
df['vitamins']       = vitamins
df['is_in_stock']    = is_in_stock
df['harvest_year']   = harvest_year
df['measures']       = measures

# change data frame to .csv file
df.to_csv("./realfinal.csv", encoding='utf8')
