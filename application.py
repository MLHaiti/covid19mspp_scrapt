import requests
from bs4 import BeautifulSoup

import tabula


from PIL import Image
import sys

import pyocr
import pyocr.builders

import urllib

#lets scrapt all link in the mssp web site

url= 'https://mspp.gouv.ht/newsite/documentation.php/'
base_url = 'https://mspp.gouv.ht/newsite/'
page = requests.get('https://mspp.gouv.ht/newsite/documentation.php')
html_text = page.text


#create a BeautifulSoup instance with the html_text variable

soup = BeautifulSoup(html_text,'html.parser')


def getLinks(mysoup):
    a_elements = mysoup.find_all('a')
    _links=[]

    for a_element in a_elements:
        _links.append(a_element.get('href'))
    return _links


links = getLinks(soup)
### FILTER THE LIST
pdf_links = [x for x in links if str(x)[-3:].lower()=='pdf']
print(pdf_links)

_pdf = requests.get(base_url+pdf_links[1])
k=0
df =[]
# for pdf_link in pdf_links:
#     frame = tabula.read_pdf(base_url+pdf_links[2], multiple_tables=True,pages='all')
#     df.append(frame)
#     print(frame)

tool = pyocr.get_available_tools()[0]
builder = pyocr.builders.TextBuilder()

file = urllib.request.url2pathname(base_url+pdf_links[1])
print(file)
# txt = tool.image_to_string(
#     Image.open(file),
#     lang=lang,
#     builder=builder
# )

# print(df)


