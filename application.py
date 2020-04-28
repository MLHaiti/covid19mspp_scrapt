import requests
from bs4 import BeautifulSoup

import tabula


from datetime import datetime

from helper import increment_msppdate, read_department_report, get_right_covid19links



#lets scrapt all link in the mssp web site

#URL format for Bulletin du 7 Avril 2020 de la surveillance du nouveau Coronavirus 2019(COVID-19)

start_date = '01-04-2020'




data = get_right_covid19links(start_date)
#init_date ='04-04-2020'


#df = read_department_report('https://mspp.gouv.ht/site/downloads/Sitrep '+init_date+'.pdf')

