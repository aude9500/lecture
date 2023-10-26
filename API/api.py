import numpy as np
import pandas as pd
import psycopg2
import requests
import urllib
import json
from urllib.parse import urlencode, unquote, quote_plus
from urllib.request import urlopen
import datetime as datetime

from DB import dbtest as db


Key = 'df1b32de279143e0bd503dc26e5f02ac'
HourlyPresents='/current'
BasicUrl = 'https://api.weatherbit.io/v2.0'

def CurrentCollector():

    LAT = 37.777496
    LON = 126.880695


    params = '?' + urlencode({quote_plus("LAT"):str(LAT),
                              quote_plus("LON"):str(LON),
                              quote_plus("Key"):Key})


    FinalURL = BasicUrl + HourlyPresents + unquote(params)
    req = urllib.request.Request(FinalURL)

    response_body = urlopen(req).read()
    data = json.loads(response_body)

    DF = pd.DataFrame.from_dict(data['data'])
    del DF['ts']

    DF2=DF[['lon','lat','temp','dewpt']]

    PreNow = datetime.datetime.today()
    PreNow = PreNow.replace(second=0,minute=0,microsecond=0)
    DF2=DF2.assign(Target=PreNow)

    conn = psycopg2.connect(host=pa.host, dbname=pa.dbname, user=pa.user, password=pa.password, port=pa.port)
    cur = conn.cursor()

    Target = Result.loc[i, 'target']
    LAT = DF2.loc[0, 'lat']
    LON = DF2.loc[0, 'lon']
    Temp = DF2.loc[0,'temp']
    Dew = DF2.loc[0,'dewpt']

    # To make it sure, we only accept past data.
    if Target > Now:
        continue

    select_all_sql = f"select EXISTS(select * from solar " \
                     f"where target = TIMESTAMP '%s' AND long = %s)" % (Target, LAT, LON)

    cur.execute(select_all_sql)
    Exists = cur.fetchone()[0]

    if not Exists:
        print("Upload: ", Target, Temp, Dew)
        query = """ INSERT INTO solar (target,actual,site_id) values (TIMESTAMP '%s',%s,%s,%s) """ % (
        Target, LAT, LONG, TEMP, Dew)
        cur.execute(query)
    else:
        print("Duplicated ", Target, Temp, Dew)
        query = """ UPDATE WEATHER SET temp = %s and dewpt = %s where target = TimeSTAMP '%s' AND lat = %s AND lon=%s """ % (Temp,Dew,Target,LAT, LON))


conn.commit()
cur.close()
conn.close()



    return DF2


if __name__ == '__main__':
    CurrentCollector()
