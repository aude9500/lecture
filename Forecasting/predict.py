import pandas as pd
import numpy as np
import os
import random
import joblib



def DataReader(Loc, FileName):
    Path = os.path.join(Loc, FileName)     #내가 받아들일 파일 경로로 만들어줌
    TempWeather = pd.read_csv(Path)
    TempWeather["DeliveryDT"] = pd.to_datetime(TempWeather["DeliveryDT"],format='%Y-%m-%d %H:%M:%S',utc=False)   #날짜 형식 변경

    return TempWeather



import pandas as pd
import numpy as np
from Forecasting import predict as pr       #main은 Forecasting파일 밖에 있으니깐 from을 사용
from sklearn.ensemble import RandomForestRegressor
import params as pa
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split



###
def trainer():
    File = "RenewableHist.csv"
    Solar = pr.DataReader(pa.Loc, File)
    Solar = Solar.sort_values(by=["DeliveryDT"], ascending=[True])

    FileList = os.listdir(pa.Loc)
    Saver = []

    for f in FileList:
        if f[0:11] == "WeatherHist":
            Data = pr.DataReader(pa.Loc, f)
            Saver.append(Data)

    Weather=pd.concat(Saver,ignore_index=True)
    Weather = Weather.sort_values(by=["DeliveryDT"],ascending=[True])
    Weather.index = range(0,len(Weather))
    # 35, 36데이터 합치기
    del Weather["#"]
    del Weather["WeatherHistId"]


    Col = ['pres', 'slp','wind_spd','wind_dir', 'temp', 'app_temp','vis','precip','snow','uv','solar_rad','vapor','snow_depth']

    Unique = Weather['WeatherStationId'].unique()

    for i in range(0,len(Unique)):
        Temp = Weather[Weather["WeatherStationId"]== Unique[i]]     #id가 35면 temp에 저장
        del Temp["WeatherStationId"]                                #WeatherStationId 열 삭제
        for cc in Col:
            Temp =  Temp.rename(columns={cc: cc + '_' +str(Unique[i])})     #id35데이터들의 열 이름에 35추가
        if i == 0:
            Saver=Temp.copy()       # i가 0이면 Saver에 Temp 복사

        else:
            Saver=pd.merge(Saver,Temp, how='inner',on="DeliveryDT")     # i가 1이라면 Saver(35)와 Temp(36)를 합침


    Total = pd.merge(Solar, Saver, how='inner',on="DeliveryDT")
    Total = Total.sort_values(by=["DeliveryDT"],ascending=[True])
    Total.index = range(0,len(Total))
    Total=Total.fillna(-9999)
    Total=Total.loc[60000:63528,]

    machine = RandomForestRegressor(
        n_estimators=1000,
        criterion="squared_error",
        max_depth=30,
        n_jobs=4,
        verbose=1
    )




    Y_train = Total["MW"]
    X_train = Total.copy()
    del X_train["MW"]
    del X_train["DeliveryDate"]
    del X_train["DeliveryDT"]



    machine.fit(X_train, Y_train)
    importances = machine.feature_importances_
    pred = machine.predict(X_train)
    pred = np.round(pred, 2)        #소수점 2자리까지 반올림

    SE = np.abs(Y_train, - pred) * np.abs(Y_train - pred)
    MSE = np.mean(SE)
    RMSE = np.sqrt(MSE)

    plt.figure(1)
    plt.plot(range(0,len(Y_train)),Y_train,label="Actual")
    plt.plot(range(0, len(Y_train)), pred, label="Prediction")
    plt.legend()
    plt.title(RMSE)
    plt.grid(True)
    plt.draw()
    plt.show(block=False)

    x_train, x_test, y_train, y_test = train_test_split(X_train,Y_train, shuffle=False,test_size = 0.1,random_state =0)

    machine.fit(X_train, Y_train)
    importances = machine.feature_importances_
    pred = machine.predict(x_test)
    pred = np.round(pred, 2)

    SE = np.abs(y_test, - pred)*np.abs(y_test - pred)
    MSE = np.mean(SE)
    RMSE = np.sqrt(MSE)

    plt.figure(2)
    plt.plot(range(0, len(y_test)), Y_train, label="Actual")
    plt.plot(range(0, len(y_test)), pred, label="Prediction")
    plt.legend()
    plt.title(RMSE)
    plt.grid(True)
    plt.draw()
    plt.show(block=False)

    print(Total)

    return[]











