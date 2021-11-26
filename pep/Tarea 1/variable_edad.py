# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 13:33:38 2021

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

#Sacamos la media y desviació tipica de la variable Edad 
necesidades_formativas_2021.Edad
np.mean (necesidades_formativas_2021.Edad) 
np.std (necesidades_formativas_2021.Edad)

#Forma Python 
necesidades_formativas_2021.Edad.mean()
necesidades_formativas_2021.Edad.std()
necesidades_formativas_2021.Edad.describe()

plt.hist(necesidades_formativas_2021.Edad) 

#Plot
x=necesidades_formativas_2021.Edad      #meto la variable dentro de un objeto
x=necesidades_formativas_2021['Edad']

#Representación gráfica
plt.hist(x,edgecolor='black',bins=10)
plt.xticks(np.arange(25, 66, step=5)) #xticks define las ticks del eje x tambien hay del eje y. Si quiere definir la lista para llegar a 9000 hay que poner 10000 porque no llega ha. 
plt.title('Figura 1. Franjas de Edad') #Poner el Titulo
plt.ylabel('Frecuencia')  #Nombrar el eje y 
plt.xlabel('Edades') #Nombrar el eje X
plt.show() #cierra el gráfico 

res = necesidades_formativas_2021.Edad.describe()
res['mean']    #Sacar la media 

print(round(res[1],1)) #Para redondear

#Store parametres as numbers

#Histogram Figure 2
plt.hist(x, bins=10, edgecolor='black')
plt.xticks(np.arange(25, 66, step=5))
plt.title('Figura 1. Franjas de Edad'
          '\n'
          ' Cooperativas de Enseñanza Pertenecientes a la UCEV')
plt.ylabel('Frecuencia')
plt.xlabel('Edad')
#textstr = ('Mean = 48\nS.D.= 10 \nn = 133')
#plt.text (58,23, textstr)
# Add reference lines and store their names in label for later legend
#plt.axvline(x=48, linewidth=1, linestyle= 'solid', color="red", label='Mean')


#histogram ver3
#plt.hist(x, bins=10, edgecolor='black')
#plt.xticks(np.arange(25, 66, step=5))
#plt.title('Figura 1. Franjas de Edad'
  #        '\n'
  #        ' Cooperativas de Enseñanza Pertenecientes a la UCEV')
#plt.ylabel('Frecuencia')
#plt.xlabel('Edad')

#props = dict(boxstyle='round', facecolor='white',lw=0.5)
#textstr = '$\mathrm{Mean}=%.0f$\n$\mathrm{S.D.}=%.0f$\n$\mathrm{n}=%.0f$'%(48 , 10 , 133)
#plt.text (58,23, textstr , bbox=props)
#plt.axvline(x=48, linewidth=1, linestyle= 'solid', color="red", label='Mean')

#figura 4 

props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(133)
plt.text (23,27, textstr , bbox=props)

# Add reference lines and store their names in label for later legend
plt.axvline(x=48, linewidth=1, linestyle= 'solid', color="red", label='Mean')
plt.axvline(x=48-10, linewidth=1, linestyle= 'dashed', color="green", label='- 1 S.D.')
plt.axvline(x=48 + 10, linewidth=1, linestyle= 'dashed', color="green", label='+ 1 S.D.')
plt. legend(loc='upper left', bbox_to_anchor=(0.73, 0.98))



plt.savefig('Bar1.svg')












