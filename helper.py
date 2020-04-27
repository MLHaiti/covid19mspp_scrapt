from datetime import datetime , timedelta
import tabula


def increment_msppdate(str_date):
    datetime_object = datetime.strptime(str_date, '%d-%m-%Y')
    datetime_inc = datetime_object + timedelta(days=1)
    date_s = datetime_inc.strftime("%d-%m-%Y")
    return {"str":date_s,"datetime": datetime_inc}


def read_department_report(url):
    df = tabula.read_pdf(url, pages="all", multiple_tables=True)
    '''generally department_report is in the first dataframe '''
    ##data = df[0].dropna(thresh=2)
    data = df[0].dropna()
    data.iloc[:,0] = data.iloc[:,0].str.replace('Grand Anse', 'Grand-Anse', regex=False)
    data.iloc[:,0] = data.iloc[:,0].str.replace('Grand Total', 'Grand-Total', regex=False)
    data = data[data.columns[0:]].apply(
    lambda x: ' '.join(x.astype(str)),
    axis=1)
    data = data.str.split(' ', expand=True)
    return data