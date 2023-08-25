import requests
from bs4 import BeautifulSoup
url = "https://www.ketto.org/"

r= requests.get(url)
htmlContent= r.content
#print(htmlContent)
soup=BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)
title=soup.title 
anchors=soup.find_all('p6')
print(anchors)