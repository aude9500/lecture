import pandas as pd
import numpy as np
from Forecasting import predict as pr       #main은 Forecasting파일 밖에 있으니깐 from을 사용
from sklearn.ensemble import RandomForestRegressor
import params as pa
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split



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