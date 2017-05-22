from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import time

Base_Urls = ['http://mirmarketa.ru/', 'https://vk.com/vezhlivaya_ledi', 'http://gadget-awesome.ru/katalog/aksessuari/dlya-avtomobilistov/vezhlivaya-ledi.html', 'http://polonex.ru/products/podsvetka-na-avto-vezhlivaya-ledi', 'http://spasibo-avto.ru/aksessyar-vezhlivaya-ledi.html']
for Base_Url in Base_Urls:
    html = urllib.request.urlopen(Base_Url)
    soup = BeautifulSoup((html.read()),'lxml')
    html_soup = soup.prettify()

    title = soup.head.title
    a = soup.findAll(attrs={'name' : re.compile("[Kk][Ee][Yy][Ww][Oo][Rr][Dd][Ss]")})
    b = soup.findAll(attrs={'name' : re.compile("[Dd][Ee][Ss][Cc][Rr][Ii][Pp][Tt][Ii][Oo][Nn]")})

    f = open('text.txt', 'a')

    f.write(str(Base_Url) + '\n')
    f.write(str(title) + '\n')
    f.write(str(a) + '\n')
    f.write(str(b) + '\n')

    f.close()
    time.sleep(5)
#print(a)

#Urls = open('file1.txt', 'r')
#Urls1 = Urls.read()
#html = urllib.request.urlopen(Urls1)
#
#print(html)
#
#html = requests.get(str(Urls))
#print (html.status_code) # Код ответа  
#print (html.headers) # Заголовки ответа
#print (html.content) # Тело ответа
#soup = BeautifulSoup(''.join(html.read()),'lxml')
#html_soup = soup.prettify()
#print(html_soup)
