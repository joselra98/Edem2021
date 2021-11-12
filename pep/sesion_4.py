# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 20:29:58 2021

@author: Jose
"""

reset -f

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

# Describir la variable de ventas (cnt) de los dos años
wbr.cnt.describe()

x=wbr['cnt']

plt.hist(x, edgecolor='black')
ticks=np.arange(0,10000,1000)
plt.xticks(ticks)

#Representación gráfica
plt.hist(x,edgecolor='black',bins=10)
plt.xticks(np.arange(0, 10000, step=1000)) #xticks define las ticks del eje x tambien hay del eje y. Si quiere definir la lista para llegar a 9000 hay que poner 10000 porque no llega ha. 
plt.title('Figure 1. Daily Bicicle rentals in washington') #Poner el Titulo
plt.ylabel('Frecuencia')  #Nombrar el eje y 
plt.xlabel('Numbers of Rentals bycicle') #Nombrar el eje X
plt.show() #cierra el gráfico 


res = wbr.cnt.describe()
res['mean']    #Sacar la media 


print(round(res[1],1)) #Para redondear


#Store parametres as numbers

#Histogram Figure 2
plt.hist(x, bins=10, edgecolor='black')
plt.xticks(np.arange(0, 10000, step=1000))
plt.title('Figure 1. Daily Bicycle rentals in Washington DC'
          '\n'
          'by Capital bikeshare.2011 - 2012')
plt.ylabel('Frecuency')
plt.xlabel('Number of rented bicycles')
textstr = ('Mean = 4504\nS.D.= 1937 \nn = 731')
plt.text (6500,110, textstr)
# Add reference lines and store their names in label for later legend
plt.axvline(x=4504, linewidth=1, linestyle= 'solid', color="red", label='Mean')

#histogram ver3
plt.hist(x, bins=10, edgecolor='black')
plt.xticks(np.arange(0, 10000, step=1000))
plt.title('Figure 3. Daily Bicycle rentals in Washington DC'
'\n'
'by Capital bikeshare. 2011 - 2012')
plt.ylabel('Frecuency')
plt.xlabel('Number of rented bicycles')

props = dict(boxstyle='round', facecolor='white',lw=0.5)
textstr = '$\mathrm{Mean}=%.1f$\n$\mathrm{S.D.}=%.1f$\n$\mathrm{n}=%.0f$'%(m, sd, n)
plt.text (6500,110, textstr , bbox=props)
plt.axvline(x=m, linewidth=1, linestyle= 'solid', color="red", label='Mean')


