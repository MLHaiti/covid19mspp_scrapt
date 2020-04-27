from datetime import datetime , timedelta
import tabula


def increment_msppdate(str_date):
    datetime_object = datetime.strptime(str_date, '%d-%m-%Y')
    datetime_inc = datetime_object + timedelta(days=1)
    date_s = datetime_inc.strftime("%d-%m-%Y")
    return {"str":date_s,"datetime": datetime_inc}


def read_department_report(url):
    df = tabula.read_pdf(url, pages="all", multiple_tables=True)
    print(type(df[1]))
    return df[1]