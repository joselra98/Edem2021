# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 15:38:35 2021

@author: Jose
"""
reset -f

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

#Modelo 4

model4 = ols ('cnt ~ temp_celsius + windspeed_kh + hum + yr',data=wbr).fit()
 
print(model4.summary2())

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

#Instalamos el programa para instalar los datos. Libreia para generar y comparar modelos de regresion 
!pip install stargazer
from stargazer.stargazer import Stargazer 

#Juntamos los tres modelos
stargazer = Stargazer ([model1, model2,model3])
stargazer.render_html() #Hace una imagen render en HTML

#Para crear la regresion lineal de la variable weathersit hace falta dividir en tres variables con dummies 
dummies = pd.get_dummies(wbr.weathersit) #Hace un nuevo dataframe 
colnames = {1:'sunny', 2:'cloudy', 3:'rainy'} #Nombre de las columnas
dummies.rename(columns = colnames, inplace = True)
wbr = pd.concat([wbr,dummies], axis=1)

#Introducimos en nuestro modelo 6 las dummies. Para hacerlo hay que dejar una fuera que se va quedar como categoria de referencia
#Dejo fuera la variable más frecuente, en este caso sunny 


model6 = ols ('cnt ~ temp_celsius + windspeed_kh + hum + workingday + yr + cloudy + rainy',data=wbr).fit()
 
print(model6.summary2())

#Intercept:1721 cuando el resto de variables vale 0 vendemos 1721 
#Cuando es cloudy vendemos 476 biciletas menos que cuando es sunny 

#REGRESIONES LÓGISTICAS

# SI LA VARIABLE TARGET ES CUALI

#recodificamos si objetivo conseguido o no 
m=4500
print(m)
wbr.loc[ (wbr['cnt']<m ),  "goal"]= 0
wbr.loc[ (wbr['cnt']>=m ),  "goal"]= 1
plt.scatter(wbr.cnt, wbr.goal)

#Importamos la libreria . Para poder hacer regresiones con la variable dependiente cualitativa

from statsmodels.formula.api import logit

model_l1 = logit('goal ~ temp_celsius', data=wbr).fit()

print(model_l1.summary2())

#


#Modelo 7

model_l7 = logit('goal ~ temp_celsius + hum + workingday + windspeed_kh + yr + cloudy + rainy ', data=wbr).fit()

print(model_l7.summary2())

#No se leen los coecifientes de regresión logistica. en este curso
# Cuando aumenta la temperatura la probabilidad de que las ventas sean altas es mayor 
# Cuando aumenta la humedad la probabilidad de que las ventas sean altas disminuye 

# TRABAJAMOS CON LA TEMPERATURA AL CUADRADO 
#REGRESION LINEAL CUADRATICA 
# El coeficiente al cuadrado detalla lo que pasa con la variable pero solo en la parte alta del grafico
#Con esto capturamos la no linealidad del modelo lineal

wbr['temp_2'] = wbr.temp_celsius*wbr.temp_celsius

model8 = ols('cnt ~ temp_celsius + temp_2 + hum + workingday + windspeed_kh + yr + cloudy + rainy ', data=wbr).fit()

print(model8.summary2())



MIRAR DROP NA 













































