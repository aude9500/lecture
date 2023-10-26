import pandas as pd
import numpy as np
from Forecasting import predict as pr       #main은 Forecasting파일 밖에 있으니깐 from을 사용
from sklearn.ensemble import RandomForestRegressor
import params as pa
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import datetime as datetime
import sys
from apscheduler.schedulers.background import BackgroundScheduler
from API import api as api



###
if __name__ == '__main__':
    arg = sys.argv[1:]
    if len(arg) > 0:
        print(arg[1])
        StartDay = arg[1]
        EndDay = arg[2]

    else:
        StartDay = '2023-03-01'
        EndDay = '2023-03-31'

    sched = BackgroundScheduler(timezone="Asia/Seoul")
    api.CurrentCollector()
    dti = pd.date_range(start=StartDay, end=EndDay, freq="1D")

    mycrawl(dti)
    # sched.add_job(gen, 'cron', minute='33', id=Container, args=[Container], max_instances=1)
    sched.add_job(mycrawl, 'interval', minutes=3, id='Solar', args=[dti], max_instances=1)
    sched.start()

    while True:
        Now = datetime.datetime.today()
        Now = Now.replace(microsecond=0)
        print(dti[pa.rotation], Now)
        time.sleep(10)