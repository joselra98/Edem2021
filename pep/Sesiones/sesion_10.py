# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:06:40 2021

@author: Jose
"""

import os
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference 
import scipy.stats as stats


# Change working directory
os.chdir(r'C:\Users\Jose\OneDrive\Escritorio\EDEM\GitKraken\Edem2021\pep\code_and_data')
os.getcwd()

#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')
wbr.shape
wbr.head()
#QC OK

#describimos las variables
wbr.cnt.hist()
wbr.temp_celsius.hist()
plt.scatter (wbr.temp_celsius, wbr.cnt)

#Importamos la liberia de los minimos cuadrados
from statsmodels.formula.api import ols

#Primer modelo de regresion

model1 = ols ('cnt ~ temp_celsius',data=wbr).fit()

print(model1.summary2())

# Nos interesa
# lo más importante el intercet(1214) y temp_celsius(161) Esto nos indica la recta que mejor describe lo que pasa
# El intercep es el valor predicho para la variable target cuando esta vale 0. cuantas bicis vendere para una temperatura 0
# temp_celsius cuanto se incrementa la variable dependiente o target por cada incremento en una unidad de la variable predictora, es decir, incrementa 161 por cada grado que aunmente la temperatura 
# Los Pvalue. al Pvalue del intercep no le prestamos atención, pero el Pvalue de la pendiente de la temperatura es muy importante.
#Este Pvalue nos dice el nivel de significación de la pendiente de la muestra es de verdad, es decir, tienen asociación 
#R-square: 0.394. Nos esta diciendo que porcentaje de la variablidad del fenomeno podemos asociar a la varibilidad que observo en la temperatura, es decir, el 40 por ciento de la varianda la puedo explicar por la varibilidad que veo en los datos. solo sabiendo la temperatura puedo saber el 40% de las ventas
# No. observatios 731 es la n 

# Modelo de regresión velocidad del viento 

wbr.cnt.hist()
wbr.windspeed_kh.hist()
plt.scatter (wbr.windspeed_kh, wbr.cnt)

#Modelo de regresión 1b

model1b = ols ('cnt ~ windspeed_kh',data=wbr).fit()

print(model1b.summary2())

# El dia que haga 0 viento empiezo vendiendo 5000 bicis
# El windspeed_kh por cada kilometro hora que incrementa el viento, las ventas disminuyen en 87 bicicletas
#R- : 0.055 es una r muy pequeña 

#Modelo 2. Vamos a juntar varios modelos de regresión.MODELO DE REGRESIÓN LINEAL MÚLTIPLE
#Haremos un modelo teniendo en cuanta las dos cosas a la vezz

model2 = ols ('cnt ~ temp_celsius + windspeed_kh',data=wbr).fit()
 
print(model2.summary2())
 
#R_ 0.41 ha mejorado el porcentaje con respecto a temperatura. El incremento en la r2 el windspeed_kh es pequeño pero es significativo

#Modelo 3 tener en cuenta en la temperatura

wbr.hum.hist()
plt.scatter (wbr.hum, wbr.cnt)

model3 = ols ('cnt ~ temp_celsius + windspeed_kh + hum',data=wbr).fit()
 
print(model3.summary2())

#R cuadrado ha subido 5 centesimas seguimos mejorando el modelo.
#Todos los predictores son significativos 
# El coeficiente de la pendiente de windspeed_kh ha cambiado porque 

#El intercept cuando tengo dos o más predictores cuando todas las varibales introducidad en el modelo valen 0
#156 cuanto se incrementan las ventas por cada incremento de la temperatira cuando mantengo constante el efecto de las otras variables. Si yo consigo quitar el efecto viento y humedad las ventas aumentan 161 por cada grado que aumenta

#Ecuación de prediccion del modelo 3
rentals= 4084 + 162*t -72*v - 31*h

#Modelo 5

wbr.workingday.hist()
wbr.yr.hist()
plt.scatter (wbr.hum, wbr.cnt)

model5 = ols ('cnt ~ temp_celsius + windspeed_kh + hum + workingday + yr',data=wbr).fit()
 
print(model5.summary2())

#la r cuadrado_0.72
# Para interpretar variable cualitativas en un modelo lineal
# El dia en que el la temperatura, viento, humedad y el año vale 0 vendo 2006, es decir, pasar del año 2011, 2012 tiene un incremento de 2006 por lo que la media en el año 2 es de 4012 bicis
# Se puede meter variables cuali si solo tiene dos niveles. Unicamente podemos meter variables cualitativas dicotomicas, es decir, no tiene más de dos valores 
#workingday no es significatico, por lo que, no lo considero para aestudiar





















#MODELOS DE COMPLEJIDAD CRECIENTE

















 
 
 


























 
