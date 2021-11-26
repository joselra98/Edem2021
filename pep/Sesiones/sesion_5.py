# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 19:09:00 2021

@author: Jose
"""
#Clase para hacer subseting es filtrar los datos 

import os                                 #Sistema Operativo
import pandas as pd                       #Gestionar Dataframes
import numpy as np                        #Numeric python vectores matrices
import matplotlib.pyplot as plt           # graficos

#Poner donde está ubicado
os.chdir(r'C:\Users\Jose\OneDrive\Escritorio\EDEM\GitKraken\Edem2021\pep\code_and_data')  #Define la carpeta de trabajo. Se tiene que hacer lo primero 
os.getcwd()

#Insertar el archivo
wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')

#Validar los datos

wbr.shape      # Para ver la dimensionalidad de las columnas
wbr.head()     # Ver las primeras lineas de la tabla
wbr.tail()     # Ver las ultimas filas de la tabla 

#Quality Control Ok

#Limpiar la tabla para quedarme con las variables que deseo

#Hago una copia de la lita de variables que quiero 

wbr_minimal= wbr[my_vars]

#Comprabar la dimensionalidad
wbr_minimal.shape

#Guardar como un csv
wbr_minimal.tocsv('wbr_minimal_edem2020.csv')

#SELECCIONAR CASOS
#Saber la media de ventas del año 2011

#saber cuantos años hay en mydataset para ello descrino la variable año

mytable = wbr.groupby(['yr']).size()
print(mytable)

#porcentajes 
n=mytable.sum()
mytable2= (mytable/n)*100
prin=(mytable2)

#copiar las filas del año 1

wbr_2011 = wbr[wbr.yr == 0] #crear un dataset que cumpla que solo saque el año 1

#sacar ventas del primer año (cnt)

plt.hist(wbr_2011.cnt)
wbr_2011.cnt.describe()

# Histograma de las ventas del invierno de 2012. Estamos subsetting de dos condiciones 

wbr_winter_2012 = wbr[(wbr.yr == 1) & (wbr.season == 1)] #pongo las condiciones de que el año sea 2011 y sea invierno season 1

wbr_winter_2012.shape #compruebo el tamaño 

#Representamos lo obtenido 
plt.hist(wbr_winter_2012.cnt)
plt.title("Rentals in Winter 2012")
wbr_winter_2012.cnt.describe()

#Hacer un histograma en el que describa las ventas en invierno y en otoño de todos los años 

wbr_fall_winter= wbr[(wbr.season == 1) | (wbr.season == 4)] #subset en el que se describan las ventas del invierno y en el otoño

wbr_fall_winter.shape #compruebo el tamaño 

#Representamos lo obtenido 
plt.hist(wbr_fall_winter.cnt)
plt.title("Rentals in Winter and Fall 2011-2012")
wbr_fall_winter.cnt.describe()

#Limpiamos el entorno
reset -f

#Saber la media de la temperatuta y desviación in Washintong. Para ello abrimos otro dataset del campus

import os                                 #Sistema Operativo
import pandas as pd                       #Gestionar Dataframes
import numpy as np                        #Numeric python vectores matrices
import matplotlib.pyplot as plt           # graficos

#Poner donde está ubicado
os.chdir(r'C:\Users\Jose\OneDrive\Escritorio\EDEM\GitKraken\Edem2021\pep\code_and_data')  #Define la carpeta de trabajo. Se tiene que hacer lo primero 
os.getcwd()

#Insertar el archivo
wbr_ue = pd.read_csv('wbr_ue.csv', sep=';', decimal=',')

#Validar los datos

wbr.shape      # Para ver la dimensionalidad de las columnas
wbr.head()     # Ver las primeras lineas de la tabla
wbr.tail()     # Ver las ultimas filas de la tabla 

#Sacamos los descriptibos para comprobar los datos 

wbr_ue.temp_celsius.describe()

#REPRESENTAMOS PARA COMPROBAR que no hay datos raros en este caso el 99 de temperatura máxima

plt.hist(wbr_ue.temp_celsius)
plt.boxplot(wbr_ue.temp_celsius)

#Para solucionar el problema de los datos erroneos hay que limpiar la variable.Remplazar sobre una nueva columna nunca macharcar los datos  

wbr_ue['temp_celsius_c'] = wbr_ue.temp_celsius.replace(99,np.nan) #la nueva columna de datos es igual a la orginal pero cambiando los 99 por np no hay datos 
wbr_ue.temp_celsius_c.describe() #comprobamos los descriptivos para ver que no hay datos erroneos el 99 
plt.hist(wbr_ue.temp_celsius_c) #hacemos el gráfico

#Siguiente nivel de depuración. Hacer el analisis solo con las filas que tienen datos validados

wbr_ue.temp_celsius_c.dropna() #Extraemos la columna pero solo con valores validos quitando los np

plt.hist(wbr_ue.temp_celsius_c.dropna()) #hacemos el histograma quitando los valores np, es decir, los que no hay 

#Hacer un dropna() de todo quita todos los ratos

