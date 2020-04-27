import requests
from bs4 import BeautifulSoup

import tabula


from datetime import datetime

from helper import increment_msppdate, read_department_report



#lets scrapt all link in the mssp web site

#URL format for Bulletin du 7 Avril 2020 de la surveillance du nouveau Coronavirus 2019(COVID-19)
site = "https://mspp.gouv.ht/site/downloads/"

start_date = '29-02-2020'


st = increment_msppdate(start_date)

print(st)

end1 ='Sitrep 05-04-2020.pdf'

dataf = read_department_report(site+end1)



