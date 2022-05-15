import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

M = np.array([[0.78084565, 0.98528035, 0.43712711],
       [0.50195108, 0.43392577, 0.13968129],
       [0.3039054 , 0.2468346 , 0.21727261]])

d = pd.DataFrame(M)
d["char"] = np.array(["a","b","c"])
d.sum(axis=1)

## Ejercicios
#
#1. Calcula la suma de todas las filas como en el ejemplo anterior.
#2. Crea un dataframe de 4x10 y calcula su media y desviación estándar para cada columna.
#3. Crea un dataframe con datos mixtos (columnas de distintos tipos). Luego separa el dataframe en dataframes de columnas del mismo tipo.
#4. Investigar cómo puedo obtener una columna de un DataFrame.

# 1.
print(d.sum(axis=0))

# 2.
rand_matrix = np.random.rand(4,10)
dataframe = pd.DataFrame(rand_matrix)
col_mean = dataframe.mean()
col_std = dataframe.std()

#print(col_mean)
#print(col_std)

#print(dataframe.describe())

df = pd.DataFrame({
    'Name': ["Anish","Rabindra","Manish","Samir","Binam"],
    'Age': [18,23,54,67,12],
    'Grades': [10,5,8,6,9],
    'LastName': ["George","Ali","Tyson","Jones","Holmes"]
})

#type_dct = {str(k): list(v) for k, v in df.groupby(df.dtypes, axis=1)}

string_df = df.groupby(['Name', 'LastName']).groups
numeric_df = df.groupby(['Age', 'Grades']).groups

print(string_df)
print(numeric_df)

# pandas.DataFrame
#     Display number of rows, columns, etc.: df.info()
#     Get the number of rows: len(df)
#     Get the number of columns: len(df.columns)
#     Get the number of rows and columns: df.shape
#     Get the number of elements: df.size
#     Notes when specifying index
# pandas.Series
#     Get the number of elements: len(s), s.size

# Dividir un DataFrame usando la indexación de filas
#     first_half = dt.iloc[:2,:]
#     second_half = dt.iloc[2:,:]

# Dividir el DataFrame utilizando el método groupby()
#     groups = df.groupby(df.Size)
#     ms_df = groups.get_group("S")
#     mba_df=groups.get_group("M")
#     phd_df=groups.get_group("XS")
#     Divide el DataFrame df en tres partes en función del valor de la columna Size.
#     Las filas con el mismo valor de la columna Size se colocarán en el mismo grupo.
#     La función groupby() formará grupos basados en el valor de la columna Size. 
#     Luego extraemos las filas agrupadas por el método groupby() utilizando el método get_group().

# Dividir el DataFrame usando el método sample()
#     random_df = df.sample(frac=0.4,random_state=60)
#     Muestrea aleatoriamente el 40% de las filas del DataFrame adfd y luego muestra el DataFrame formado por las filas muestreadas. 
#     El random_state se establece para asegurar que obtenemos las mismas muestras aleatorias en el muestreo cada vez.