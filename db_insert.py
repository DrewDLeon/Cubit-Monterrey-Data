import pandas as pd
from db_params import params
from sqlalchemy import create_engine, URL
from sqlalchemy.types import *

df_schema = {
    "id_accidente":INT,
    "fecha":DATE,
    "hora":INT,
    "dia":VARCHAR(20),
    "tipo":VARCHAR(30),
    "clima":VARCHAR(20),
    "calle":VARCHAR(60),
    "cruce":VARCHAR(60),
    "sentido":VARCHAR(30),
    "colonia":VARCHAR(40),
    "municipio":VARCHAR(30),
    "longitud":FLOAT(9,6),
    "latitud":FLOAT(9,6)
}

def db_push(df):
    df = df.reindex(columns=['fecha', 'hora', 'dia', 'tipo', 'clima', 'calle', 'cruce', 'sentido', 'colonia', 'municipio', 'longitud', 'latitud'])
    print(df.head(30))
    df.to_csv("C:/Users/Andres/Desktop/Code/Hackathon/Tigre Hacks/Docs/dataFiltered.csv")

    user = params('doadmin')
    engine = create_engine(f'mysql+mysqlconnector://{user.user}:{user.password}@{user.host}:{user.port}/{user.database}')

    
    df.to_sql(
        'tbl_accidentes',
        con=engine,
        if_exists='append',
        index=False,
        dtype=df_schema
    )
    print('Base de Datos Actualizada!')




