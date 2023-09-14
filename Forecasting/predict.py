import pandas as pd
import numpy as np
import os

def DataReader(Loc, FileName):
    Path = os.path.join(Loc, FileName)     #내가 받아들일 파일 경로로 만들어줌
    TempWeather = pd.read_csv(Path)
    TempWeather["DeliverDT"] = pd.to_datetime(TempWeather["DeliveryDT"],format='%Y-%m-%d %H:%M:%S',utc=False)   #날짜 형식 변경

    return TempWeather
