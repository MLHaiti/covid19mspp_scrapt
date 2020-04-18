import requests
from bs4 import BeautifulSoup

#lets scrapt all link in the mssp web site

url= 'https://mspp.gouv.ht/newsite/documentation.php'
page = requests.get('https://mspp.gouv.ht/newsite/documentation.php')
html_text = page.text
print(html_text)