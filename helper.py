from datetime import datetime , timedelta
import tabula
from  requests import request
import pandas as pd


def increment_msppdate(str_date):
    datetime_object = datetime.strptime(str_date, '%d-%m-%Y')
    datetime_inc = datetime_object + timedelta(days=1)
    date_s = datetime_inc.strftime("%d-%m-%Y")
    return {"str":date_s,"datetime": datetime_inc}


def read_department_report(url):
    df = tabula.read_pdf(url, pages="all", multiple_tables=True)
    '''generally department_report is in the first dataframe '''
    if isinstance(df, pd.DataFrame) :
        data = df.dropna(thresh=2, axis='index')
    else:
        data = df[0].dropna(thresh=2, axis='index')

    data = data[data.isna().sum(axis=1) < 3]
    data.iloc[:,0] = data.iloc[:,0].astype(str).str.replace('Grand Anse', 'Grand-Anse', regex=False)
    data.iloc[:,0] = data.iloc[:,0].astype(str).str.replace('Grand Total', 'Grand-Total', regex=False)
    data = data[data.columns[0:]].apply(
    lambda x: ' '.join(x.astype(str)),
    axis=1)
    data = data.astype(str).str.split(' ', expand=True)
    return data

def is_pdf_link(url):
    response = request(method='GET', url=url)
    content_type = response.headers.get('content-type')
    if 'application/pdf' in content_type:
        return True
    else:
        return False

def get_right_covid19links(str_start_date):
    base_url = "https://mspp.gouv.ht/site/downloads/"
    pdf_links =[]
    now = datetime.now()
    init_date = str_start_date
    df = None
    while increment_msppdate(init_date)['datetime'] <=  now :
        link = base_url+'Sitrep '+init_date+'.pdf'
        if is_pdf_link(link) :
            pdf_links.append(link)
            # I will read a dataframe inside it
            dataframe = read_department_report(link)
            dataframe.to_csv('mssp_'+init_date+'.csv')
            if dataframe.shape[0]>6 :
                if df is None :
                    df = dataframe
                else:
                    df = df.append(dataframe)
        init_date = increment_msppdate(init_date)['str']
    df = df.dropna(axis='columns',thresh=1)
    df.to_csv('mspp.csv')
    return pdf_links