from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import time

#proba

Base_Urls = ['https://zaochnik.ru/diplomnaya-rabota/?utm_expid=56993635-57.QKZNuOljSMitMb7Bu2tUqw.0&utm_referrer=https%3A%2F%2Fwww.google.ru%2F', 'https://finzakaz.ru/diplomnaya-zakaz.htm', 'http://www.mosdiplom.ru/nashi-uslugi-studentam/diplomnye-raboty-na-zakaz', 'https://bestworks.ru/', 'http://artdiplom.club/']
for Base_Url in Base_Urls:
    html = urllib.request.urlopen(Base_Url)
    soup = BeautifulSoup((html.read()),'lxml')
    html_soup = soup.prettify()

    title = soup.head.title
    a = soup.findAll(attrs={'name' : re.compile("[Kk][Ee][Yy][Ww][Oo][Rr][Dd][Ss]")})
    b = soup.findAll(attrs={'name' : re.compile("[Dd][Ee][Ss][Cc][Rr][Ii][Pp][Tt][Ii][Oo][Nn]")})

    f = open('text.txt', 'a')

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