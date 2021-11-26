# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:40:34 2021

@author: Jose
"""
reset -f

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

#Sacamos la media y desviació tipica de la variable Grandaria
necesidades_formativas_2021.Grandaria
np.mean (necesidades_formativas_2021.Grandaria) 
np.std (necesidades_formativas_2021.Grandaria)

#Forma Python 
necesidades_formativas_2021.Grandaria.mean()
necesidades_formativas_2021.Grandaria.std()
necesidades_formativas_2021.Grandaria.describe()

plt.hist(necesidades_formativas_2021.Grandaria) 

#Plot
x=necesidades_formativas_2021.Grandaria      #meto la variable dentro de un objeto
x=necesidades_formativas_2021['Grandaria']

#Representación gráfica
plt.hist(x, edgecolor='black',bin=4)
plt.xticks(np.arange(0, 4, step=1)) #xticks define las ticks del eje x tambien hay del eje y. Si quiere definir la lista para llegar a 9000 hay que poner 10000 porque no llega ha. 
plt.title('Figura 1. Tamaño de las Empresas') #Poner el Titulo
plt.ylabel('Frecuencia')  #Nombrar el eje y 
plt.xlabel('Franjas Tamaño Cooperativas') #Nombrar el eje X
plt.show() #cierra el gráfico 

res = necesidades_formativas_2021.Grandaria.describe()
res['mean']    #Sacar la media 

print(round(res[1],1)) #Para redondear

#Store parametres as numbers

#Histogram Figure 2
plt.hist(x, bins=4, edgecolor='black')
plt.xticks(np.arange(1, 5, step=1))
plt.title('Figura 1. Tamaño de las Empresas'
          '\n'
          ' Cooperativas de Enseñanza Pertenecientes a la UCEV')
plt.ylabel('Frecuencia')
plt.xlabel('Tamaño de las Cooperativas')
textstr = ('1 = 1-10\n2= 11-50 \n3 = 51-250\n4 = >250')
plt.text (1,40, textstr)
#Add reference lines and store their names in label for later legend
plt.axvline(x=2.6, linewidth=1, linestyle= 'solid', color="red", label='Mean')


#histogram ver3
#plt.hist(x, bins=10, edgecolor='black')
#plt.xticks(np.arange(25, 66, step=5))
#plt.title('Figura 1. Franjas de Edad'
  #        '\n'
  #        ' Cooperativas de Enseñanza Pertenecientes a la UCEV')
#plt.ylabel('Frecuencia')
#plt.xlabel('Edad')

#props = dict(boxstyle='round', facecolor='white',lw=0.5)
#textstr = '$\mathrm{1}=%.0f$\n$\mathrm{2}=%.0f$\n$\mathrm{3}=%.0f$\n$\mathrm{4}=%.0f$'%(1-10 , 11-50 , 51-250. >250)
#plt.text (1,40, textstr , bbox=props)
#plt.axvline(x=2.6, linewidth=1, linestyle= 'solid', color="red", label='Mean')

#figura 4 

props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(133)
plt.text (1,62, textstr , bbox=props)

# Add reference lines and store their names in label for later legend
plt.axvline(x=2.6, linewidth=1, linestyle= 'solid', color="red", label='Mean')
plt.axvline(x=2.6-0.86, linewidth=1, linestyle= 'dashed', color="green", label='- 1 S.D.')
plt.axvline(x=2.6 + 0.86, linewidth=1, linestyle= 'dashed', color="green", label='+ 1 S.D.')
plt. legend(loc='upper left', bbox_to_anchor=(0.73, 0.98))


plt.savefig('Bar1.svg')