import psycopg2                          #pip install psycopg2-binary
from sqlalchemy import create_engine     #pip install sqlalchemy
import params as pa
import pandas as pd
import os

def DataReader(Schema, Table, Col, Value):
    query =(""" SELECT * from "%s"."%s" where "%s" = '%s' """ %(Schema, Table, Col, Value))
    # 쿼리문은 따옴표 3개, copy paste는 하면 안됨

    conn_string = 'postgresql://' + pa.user + ":" + pa.password + "@" + pa.host + ":" + str(pa.port) + "/" + pa.dbname


    alchemyEngine = create_engine(conn_string)
    dbConnection = alchemyEngine.connect()
    Data = pd.read_sql(query, con=dbConnection)
    dbConnection.close()                            #계속 연결되어있으면 db가 바꼈을 때 반응 안하는 경우가 있음 그래서 끊어줌
    alchemyEngine.dispose()


    return Data


if __name__ == '__main__':
    Schema = 'public'
    Table = "student"
    Col = 'name'
    Value = "Moon"
    Data = DataReader(Schema, Table, Col, Value)

    print("a")


