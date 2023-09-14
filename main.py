import pandas as pd
import numpy as np
from Forecasting import predict as pr       #main은 Forecasting파일 밖에 있으니깐 from을 사용
import params as pa
import os
import glob

if __name__ == '__main__':
    File = "Solar_4.csv"
    Solar = pr.DataReader(pa.Loc, File)

    FileList = os.listdir(pa.Loc)
    Saver = []

    for f in FileList:
        if f[0] == "W":
            Data = pr.DataReader(pa.Loc, f)
            Saver.append(Data)

            Weather=pd.concat(Saver,ignore_index=True)
            Weather = Weather.sort_values(by=["DeliveryDT"],ascending=[True])
            Weather.index = range(0,len(Weather))









    merge_df = pd.DataFrame()

    file_list = glob.glob(pa.Loc2)

    for f in file_list:
        df = pd.read_csv(f)
        merge_df = merge_df.append(df, ignore_index=True)


    print('a')

    # print(Solar)
    # pd.set_option('display.width',5000)
    # pd.set_option('display.max_rows',5000)
    # pd.set_option('display.max_columns',5000)



