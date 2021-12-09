# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 19:05:28 2021

@author: Jose
"""

#load basiclibraries
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


#La temperatura va tener un impacto en las ventas. 
x=wbr['temp_celsius']
plt.hist(x, bins=10, edgecolor='black')

#El clima en washintong está muy polarizado, es decir, hay dos temporadas hay días frías y días calidos

#Scaterplot. X temperatura y en la Y las centas 
plt.figure(figsize=(5,5)) #Para hacerlo cuadrado
plt.scatter(wbr.temp_celsius, wbr.cnt, s=20, facecolors='none', edgecolors='C0') #S=20 Es el tamaño
plt.ylabel('Daily Rentals')
plt.xlabel('Temperature (Centigrades)')

#La correlacion lineal entre dos variables es con pearson que va de -1 a 1.

from scipy.stats.stats import pearsonr

x=wbr.temp_celsius
y=wbr.cnt
pearsonr(x,y) #el primer numero es el coeficiente de correlacion lineal de pearson y el segundo número es el pvalue hay mucha asociacion  


r, p_val = pearsonr(x, y)

print (r,p_val)

n =  len (wbr.cnt) #longitud de la varibale ventas 
print ('r, round(r,3), ''P.Val:', round(p_val,3), 'n:', n)

#Representacion 
plt.figure(figsize=(5,5)) #Para hacerlo cuadrado
plt.scatter(wbr.temp_celsius, wbr.cnt, s=20, facecolors='none', edgecolors='C0', c=wbr.yr) #S=20 Es el 
plt.xticks(np.arange(0, 40, step=5))
plt.yticks(np.arange(0, 10000, step=1000))
plt.ylabel('Daily Rentals')
plt.xlabel('Temperature (Centigrades)')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (3,7000, textstr , bbox=props)
plt.show()

plt.figure(figsize=(5,5)) #Para hacerlo cuadrado
plt.scatter(wbr.temp_celsius, wbr.cnt, s=20, facecolors='none', edgecolors='C0', c=wbr.season) #S=20 Es el 
plt.xticks(np.arange(0, 40, step=5))
plt.yticks(np.arange(0, 10000, step=1000))
plt.ylabel('Daily Rentals')
plt.xlabel('Temperature (Centigrades)')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (3,7000, textstr , bbox=props)
plt.show()


#Correlacion lineas de las ventas de alquiler con el viento 

#El veinto va tener un impacto en las ventas. 
x=wbr['windspeed_kh']
plt.hist(x, bins=10, edgecolor='black')

#Scaterplot. X temperatura y en la Y las centas 
plt.figure(figsize=(5,5)) #Para hacerlo cuadrado
plt.scatter(wbr.windspeed_kh, wbr.cnt, s=20, facecolors='none', edgecolors='C0') #S=20 Es el tamaño
plt.ylabel('Daily Rentals')
plt.xlabel('Temperature (Centigrades)')

x=wbr.windspeed_kh
y=wbr.cnt
pearsonr(x,y) #el primer numero es el coeficiente de correlacion lineal de pearson y el segundo número es el pvalue hay mucha asociacion  


r, p_val = pearsonr(x, y)

print (r,p_val)

n =  len (wbr.cnt) #longitud de la varibale ventas

#Representacion 
plt.figure(figsize=(5,5)) #Para hacerlo cuadrado
plt.scatter(wbr.windspeed_kh, wbr.cnt, s=20, facecolors='none', edgecolors='C0') #S=20 Es el 
plt.xticks(np.arange(0, 40, step=5))
plt.yticks(np.arange(0, 10000, step=1000))
plt.ylabel('Daily Rentals')
plt.xlabel('Wind Speed (Kilometres)')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (25,7000, textstr , bbox=props)
plt.show()

#Importa másla temperatura que el viento aunque ambos son significativos. 

#Miramos si tiene correlacion la weather situaion con el viento

plt.figure(figsize=(5,5)) #Para hacerlo cuadrado
plt.scatter(wbr.windspeed_kh, wbr.cnt, s=20, facecolors='none', edgecolors='C0', c= wbr.wathersit) #S=20 Es el 
plt.xticks(np.arange(0, 40, step=5))
plt.yticks(np.arange(0, 10000, step=1000))
plt.ylabel('Daily Rentals')
plt.xlabel('Wind Speed (Kilometres)')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (25,7000, textstr , bbox=props)
plt.show()

#Una cosa no explica la otra 
























