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

    return[]


if __name__ == '__main__':
    CurrentCollector()
