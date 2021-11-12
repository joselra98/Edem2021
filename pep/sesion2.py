# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 16:49:25 2021

@author: Jose
"""
reset -f 

import os                                 #Sistema Operativo
import pandas as pd                       #Gestionar Dataframes
import numpy as np                        #Numeric python vectores matrices
import matplotlib.pyplot as plt           # graficos

# Change working directory 

os.chdir(r'C:\Users\Jose\OneDrive\Escritorio\EDEM\GitKraken\Edem2021\pep\code_and_data')  #Define la carpeta de trabajo. Se tiene que hacer lo primero 
os.getcwd()

#Leer un csv 

rentals_2011 = pd.read_csv ('washington_bike_rentals_2011.csv', sep=';', decimal=',')  #Cargar el archivo csv 

#Validar los datos

rentals_2011.shape      # Para ver la dimensionalidad de las columnas
rentals_2011.head()     # Ver las primeras lineas de la tabla
rentals_2011.tail()     # Ver las ultimas filas de la tabla 

#Quality Control Ok

#Sacar la variable ventas (cnt) es un atributo que está guardado dentro del objeto rentals_2011
rentals_2011.cnt
np.mean (rentals_2011.cnt)  #Sacar la media de ventas al día. Para ello llamamos a la liberia np
np.std (rentals_2011.cnt)    #Sacar la desviación tipica de las ventas 

#Hacer la media y la desviación en modo python
rentals_2011.cnt.mean()
rentals_2011.cnt.std()
rentals_2011.cnt.describe()    #Saca todos los estadisticos descriptivos 25% el primer cuartil el valor de ventas que deja detras el 25% de los casos, 50% mediana

#Para representar una variable cuantitativa con la media y la desviación tipica, como mucho el minimo y máximo 

#Describir gráficamente una variable cuantitativa 
# Variable cuantitativa númericamente con la media y desviación tipica y gráficamente con Histograma
plt.hist(rentals_2011.cnt) 

# Forma de python
rentals_2011.cnt.hist

y=rentals_2011.loc[: , 'casual']
x=rentals_2011.loc[: , 'registered' ]

#Plot
x=rentals_2011.cnt      #meto la variable dentro de un objeto
x=rentals_2011['cnt']

#Representación gráfica
plt.hist(x,edgecolor='black',bins=20)
plt.xticks(np.arange(0, 7000, step=1000)) #xticks define las ticks del eje x tambien hay del eje y. Si quiere definir la lista para llegar a 9000 hay que poner 10000 porque no llega ha. 
plt.title('Figure 1. Registered rental in Washington') #Poner el Titulo
plt.ylabel('Frecuencia')  #Nombrar el eje y 
plt.xlabel('Numbers of Rentals') #Nombrar el eje X
plt.show() #cierra el gráfico 

#Enriquecer el dataset con datos de la meteo, es decir, juntarlos

weather_2011 = pd.read_csv ('weather_washington_2011.csv', sep=';', decimal=',')  

#Validar los datos

weather_2011.shape      # Para ver la dimensionalidad de las columnas
weather_2011.head()     # Ver las primeras lineas de la tabla
weather_2011.tail()     # Ver las ultimas filas de la tabla 

# QC OK

#Saber los tipos de datos de un dateframe 1 soleado 2 nublado 3 lluvioso
weather_2011.dtypes

#Unir los dos dataset.Necesitamos un unico id que este en los dos (fecha,día)
#Merge two dateframe
rentals_weather_2011=pd.merge(weather_2011, rentals_2011, on='day') #Creo un tercer dataframe de ambos. day es la plabra clabe que va unir ambos por esa variable 

#Validar los datos

rentals_weather_2011.shape      # Para ver la dimensionalidad de las columnas
rentals_weather_2011.head()     # Ver las primeras lineas de la tabla
rentals_weather_2011.tail()     # Ver las ultimas filas de la tabla 

# QC OK

#Borrar una de las columnas repetidas de fecha 
del rentals_weather_2011['dteday_y']

# Cambiar el nombre de la columna de fecha que ha quedado
rentals_weather_2011 = rentals_weather_2011.rename(columns={'dteday_x': 'dteday'})

#Añadir filas 

rentals_weather_2012 = pd.read_csv('rentals_weather_2012.csv', sep=';', decimal=',')

rentals_weather_2012.shape
rentals_weather_2012.head()

#QC OK 

#Añadir filas append

rentals_weather_11_12 = rentals_weather_2011.append(rentals_weather_2012)   # el primer dateframe añadiendo el segundo 

#WE CAN MERGE THE TWO DATA FRAMES IN A NEW ONE CONTAINING SAME
#VARIABLES(COLUMNS) BUT MORE CASES(ROWS)
rentals_weather_11_12 = rentals_weather_2011.append(rentals_weather_2012,
ignore_index=True)
print (rentals_weather_11_12.shape)
print (rentals_weather_11_12.head())
print (rentals_weather_11_12.tail())


# Tricks of the trade: Column order is set alphabetically while merging
# You can restore it by doing:
rentals_weather_11_12 = rentals_weather_11_12[rentals_weather_2011.columns]

#Hacer una copia para abreviar el nombre
wbr=rentals_weather_11_12
del ( weather_2011, rentals_2011)








