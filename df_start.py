import pandas as pd
from db_insert import db_push
df = pd.read_csv("C:/Users/Andres/Downloads/incidentesviales_noviembre22.csv", low_memory=False)
    
df = pd.DataFrame(df)

# agregamos la hora completa para poder iterar con las facilidades de pandas
print('cambiando formato de hora')
df['hora'] += ':00'

# ['total_muertos','situacion_pavimento','total_lesionados','numero_infracciones','vehiculo3_muertos','vehiculo3_lesionados','vehiculo3_arresto', 'vehiculo3_cinturon','vehiculo3_edad','vehiculo3_dictamen_alcoholismo', 'vehiculo3_genero','vehiculo3_licencia','vehiculo3_modelo','vehiculo3_marca','vehiculo3_tipo','vehiculo2_muertos','vehiculo2_lesionados','vehiculo2_arresto','vehiculo2_cinturon','vehiculo2_edad','vehiculo2_dictamen_alcoholismo','vehiculo2_genero','vehiculo2_licencia','vehiculo2_modelo','vehiculo2_marca','vehiculo2_tipo','vehiculo1_muertos','vehiculo1_lesionados','vehiculo1_arresto','vehiculo1_cinturon','vehiculo1_edad','vehiculo1_dictamen_alcoholismo','vehiculo1_genero','vehiculo1_licencia','vehiculo1_modelo','vehiculo1_marca','vehiculo1_tipo','tipo_vialidad','causa']
print('borrando columnas innecesarias')
df.drop(['total_muertos','situacion_pavimento','zona','total_lesionados', 'folio','numero_infracciones','vehiculo3_muertos','vehiculo3_lesionados','vehiculo3_arresto', 'vehiculo3_cinturon','vehiculo3_edad','vehiculo3_dictamen_alcoholismo', 'vehiculo3_genero','vehiculo3_licencia','vehiculo3_modelo','vehiculo3_marca','vehiculo3_tipo','vehiculo2_muertos','vehiculo2_lesionados','vehiculo2_arresto','vehiculo2_cinturon','vehiculo2_edad','vehiculo2_dictamen_alcoholismo','vehiculo2_genero','vehiculo2_licencia','vehiculo2_modelo','vehiculo2_marca','vehiculo2_tipo','vehiculo1_muertos','vehiculo1_lesionados','vehiculo1_arresto','vehiculo1_cinturon','vehiculo1_edad','vehiculo1_dictamen_alcoholismo','vehiculo1_genero','vehiculo1_licencia','vehiculo1_modelo','vehiculo1_marca','vehiculo1_tipo','tipo_vialidad','causa'],inplace=True, axis=1)
df.dropna(axis=0, how="any", subset=None, inplace=True)

df['fecha'] = pd.to_datetime(df['fecha'])
df['hora'] = pd.to_datetime(df['hora'])
df['dia'] = df['fecha'].dt.day_name()
df['dia'] = df['dia'].astype(str)
df['hora'] = (df['hora'].dt.hour).astype(int) 

df.rename(columns = {'tipo_accidente':'tipo', 'nombre_vialidad':'calle', 'situacion_climatica':'clima'}, inplace = True)

print(df.head(30))

db_push(df)