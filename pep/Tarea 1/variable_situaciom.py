# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 18:44:36 2021

@author: Jose
"""

reset -f
# Describir una variable nóminal 
# Para describir valores cualitativos es el porcentaje y el tamaño de la muestra total 
# Para cuali Gráficos de barras o tabla de porcentajes 

import os                                 #Sistema Operativo
import pandas as pd                       #Gestionar Dataframes
import numpy as np                        #Numeric python vectores matrices
import matplotlib.pyplot as plt           # graficos

# Entramos en la carpeta donde se encuentra el archivo que vamos a utilizar 
os.chdir(r'C:\Users\Jose\OneDrive\Escritorio\EDEM')
os.getcwd()

#Leemos el archivo 

necesidades_formativas_2021 = pd.read_csv ('necesidades_formativas.csv', sep=';', decimal=',')

#Validamos los datos 

necesidades_formativas_2021.shape      # Para ver la dimensionalidad de las columnas
necesidades_formativas_2021.head()     # Ver las primeras lineas de la tabla
necesidades_formativas_2021.tail()     # Ver las ultimas filas de la tabla 

#Quality Control Ok

#crear mi tabla
# Frecuencias

mytable = necesidades_formativas_2021.groupby(['Situacion']).size()
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

bar_list = ['Socio', 'Trabajador Eventual', 'Trabajador Fijo'] #Ponemos el nombre a cada una de las barras

plt.bar(bar_list, mytable2) #Poner la longitud de las tablas 

bar_list = ['Socio', 'Trabajador Eventual', 'Trabajador Fijo']
plt.bar(bar_list, mytable2, edgecolor='black')
plt.ylabel('Porcentage')
plt.title('Figura 1. Porcentage Situación Laboral')
#plt.text (2, 70, 'n:133') #1.7 coordenada x, 50 coordenada y 

#MIRAR LA FILIGRANA EN LAS TRANSPARENCIAS
props = dict(boxstyle= 'round', facecolor= 'white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(n)
plt.text (2,70, textstr , bbox=props)

#Guardar las Figuras 
plt.savefig('bar1.eps')
plt.savefig('bar1.jpg')
plt.savefig('bar1.svg') #Formato vectorial son una serie de instrucciones que word redibuja. No pierde calidad
plt.show()