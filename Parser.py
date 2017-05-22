from bs4 import BeautifulSoup
import requests
import re
import time


for Base_Url in open(r'D:\Primer\urlForParser.txt', 'r'):
    html = requests.get(Base_Url)
    soup = BeautifulSoup(''.join(html.read()),'lxml')
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