# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 19:28:22 2021

@author: Jose
"""

# Describir una variable nóminal 
# Para describir valores cualitativos es el porcentaje y el tamaño de la muestra total 
# Para cuali Gráficos de barras o tabla de porcentajes 

import os                                 #Sistema Operativo
import pandas as pd                       #Gestionar Dataframes
import numpy as np                        #Numeric python vectores matrices
import matplotlib.pyplot as plt           # graficos

#crear mi tabla
# Frecuencias

mytable = wbr.groupby(['weathersit']).size()
print(mytable)

#Para saber el total de la tabla (n) y así sacar los porcentajes 
mytable.sum()

# Porcentajes
n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)

#Redondear los porcentajes de la tabla 
mytable3 = round(mytable2,1)
mytable3

#Hacer el gráfico de barras 
plt.bar(mytable.index, mytable2)  #bar de barras

bar_list = ['Sunny', 'Cloudy', 'Rainy'] #Ponemos el nombre a cada una de las barras

plt.bar(bar_list, mytable2) #Poner la longitud de las tablas 

bar_list = ['Sunny', 'Cloudy', 'Rainy']
plt.bar(bar_list, mytable2, edgecolor='black')
plt.ylabel('Percentage')
plt.title('Figure 1. Percentage of weather situation')
plt.text (1.7, 50, 'n:731') #1.7 coordenada x, 50 coordenada y 

#MIRAR LA FILIGRANA EN LAS TRANSPARENCIAS
props = dict(boxstyle= 'round', facecolor= 'white', lw=0.5)
twxtstr = $\mathrm{n}=%0fs$'%(n)


#Guardar las Figuras 
plt.savefig('bar1.eps')
plt.savefig('bar1.jpg')
plt.savefig('bar1.svg') #Formato vectorial son una serie de instrucciones que word redibuja. No pierde calidad
plt.show()



