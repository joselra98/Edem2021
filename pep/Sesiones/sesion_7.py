# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 17:15:16 2021

@author: Jose
"""

#Primer escernario variable cuanti vs cuali, se hace una comparacion de medias

#hipotesis la media de las rentas en working days no es igual a la media de las rentas en vacaciones

#cuando comparo dos grupos se hace un t test. Si quieres comparar más de dos grupos Anova 

reset -f

import os                                 #Sistema Operativo
import pandas as pd                       #Gestionar Dataframes
import numpy as np                        #Numeric python vectores matrices
import matplotlib.pyplot as plt           # graficos
from pandas.api.types import CategoricalDtype
import scipy.stats as stats #Para estadistica
import seaborn as sns #para hacer gráficos de más nivel 

#Poner donde está ubicado
os.chdir(r'C:\Users\Jose\OneDrive\Escritorio\EDEM\GitKraken\Edem2021\pep\code_and_data')  #Define la carpeta de trabajo. Se tiene que hacer lo primero 
os.getcwd()

#Insertar el archivo
wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')

#Compruebo la variable cuantitativa este bien sin ruido 
wbr.cnt.describe()
plt.hist (wbr.cnt)

#Comprobar que la variable cualitativa está bien y no tiene ruido
mytable = pd.crosstab(index=wbr["workingday"], columns="count")
n=mytable.sum()
mytable2 = (mytable/n)*100
plt.bar(mytable2.index, mytable2['count'])

#Calcular la media de las ventas 
wbr.groupby('workingday').cnt.mean() #Estos datos sugieren media en los dias no festivos vendemos 4330 y en los dias de trabajo 4584

#Necesitamos saber el nivel de significación de la media para saber la confianza.Para saber la hipotesis en general hay que mirar el nivel de significación
#Contrastamos a nivel poblacional(General)
#Paso1 creamos un subseting
cnt_wd= wbr.loc[wbr.workingday==1, "cnt"]  #grupo 1 nombre dataser. nombre de la variable y nombre de la variable nominal
cnt_nwd= wbr.loc[wbr.workingday==0, "cnt"] #g2

#Cargamos la libreria
import scipy.stats as stats #Para estadistica

#Paso 2 hacemos el test 

res= stats.ttest_ind(cnt_wd, cnt_nwd, equal_var = False) # comparamos las dos variables y asumimos que no son iguales por lo tanto es conservador
print (res[1])  #este dato nos permitira hacer la compración t test. Este es el P Value. el nivel de significación

# EL P VALUE: Es la probabilidad de que en realidad no haya ninguna diferencia entre los dos grupos que estamos comparando. La probalidad de que en la población de que no haya diferencias es de 0.11 (va de 0 a 1)La probabilidad de equivocarse es del 11% la máxima que aceptamos es un 0,5
# Es decir <0.5 hay diferencias >0.5 no hay diferencias (no me atrebo a decir a extrapolar la población)
#El working day no tiene impacto en las ventas. En este caso nos quedamos con H0 no hay efecto, rechazo H1

#Representacion la media de ventas para los workindays y la media de ventas para los noworkingdays con un intervalo de confianza para la media del 95%. La media es la linea verde. horizontal y punto izquiera workingdays, horizontal y punto derecha workingdays (Ambas son los intervalos de confianza donde creo que esta la media de verdad. Margen de error) Cuando los margenes de error se separan y no se solopan podemos decir que las ventas no se solpan

import seaborn as sns
import matplotlib.pyplot as plt


plt.figure(figsize=(5,5))
ax = sns.pointplot(x="workingday", y="cnt", data=wbr,ci=95, join=0)
plt.yticks(np.arange(0, 9000, step=1000))
plt.ylim(1000,8000)
plt.axhline(y=wbr.cnt.mean(),
            linewidth=1,
            linestyle= 'dashed',
            color="green")  #wbr.cnt.mean() pones la altura a la que tiene que poner la media 
props = dict(boxstyle='round', facecolor='white', lw=0.5)
ax.set_ylabel('Rentals')
plt.text(0.90,6500,'Mean:4504.3''\n''n:731' '\n' 't:1.601' '\n' 'Pval.:0.110', bbox=props)
plt.xlabel('Working Day')
plt.title('Figure 6. Average rentals by Working Day.''\n')

#Explicacion del gráfico arriba 
#DEBER Trasnformar a categorica el workingday (yes,no) y hacer la gráfica 

# COmo el pvalue es mayor a 0,05 no rechazamos la hipoteisis nula. 

#EJERCICIO
# Mismo caso que el anterior pero viendo si importa el año

#Compruebo la variable cuantitativa este bien sin ruido 
wbr.cnt.describe()
plt.hist (wbr.cnt)

#Comprobar que la variable cualitativa está bien y no tiene ruido
mytable = pd.crosstab(index=wbr["yr"], columns="count")
n=mytable.sum()
mytable2 = (mytable/n)*100
plt.bar(mytable2.index, mytable2['count'])

#Calcular la media de las ventas 
wbr.groupby('yr').cnt.mean() #Estos datos sugieren media en los dias no festivos vendemos 3405 y en los dias de trabajo  5599

#Necesitamos saber el nivel de significación de la media para saber la confianza.Para saber la hipotesis en general hay que mirar el nivel de significación
#Contrastamos a nivel poblacional(General)
#Paso1 creamos un subseting
g1= wbr.loc[wbr.yr==1, "cnt"]  #grupo 1 nombre dataser. nombre de la variable y nombre de la variable nominal
g2= wbr.loc[wbr.yr==0, "cnt"]  #g2

#Cargamos la libreria
import scipy.stats as stats #Para estadistica

#Paso 2 hacemos el test 

res= stats.ttest_ind(g1, g2, equal_var = False) # comparamos las dos variables y asumimos que no son iguales por lo tanto es conservador
print (res)  #este dato nos permitira hacer la compración t test. Este es el P Value. el nivel de significación

# EL P VALUE: Es la probabilidad de que en realidad no haya ninguna diferencia entre los dos grupos que estamos comparando. La probalidad de que en la población de que no haya diferencias es de 0.11 (va de 0 a 1)La probabilidad de equivocarse es del 10% la máxima que aceptamos es un 0,5
# Es decir <0.5 hay diferencias >0.5 no hay diferencias (no me atrebo a decir a extrapolar la población)
#El working day no tiene impacto en las ventas. En este caso nos quedamos con H0 no hay efecto, rechazo H1

#Representacion la media de ventas para los workindays y la media de ventas para los noworkingdays con un intervalo de confianza para la media del 95%. La media es la linea verde. horizontal y punto izquiera workingdays, horizontal y punto derecha workingdays (Ambas son los intervalos de confianza donde creo que esta la media de verdad. Margen de error) Cuando los margenes de error se separan y no se solopan podemos decir que las ventas no se solpan

import seaborn as sns
import matplotlib.pyplot as plt


plt.figure(figsize=(5,5))
ax = sns.pointplot(x="yr", y="cnt", data=wbr,ci=95, join=0)
plt.yticks(np.arange(0, 9000, step=1000))
plt.ylim(1000,8000)
plt.axhline(y=wbr.cnt.mean(),
            linewidth=1,
            linestyle= 'dashed',
            color="green")  #wbr.cnt.mean() pones la altura a la que tiene que poner la media 
props = dict(boxstyle='round', facecolor='white', lw=0.5)
ax.set_ylabel('Rentals')
plt.text(0.90,6500,'Mean:4504.3''\n''n:731' '\n' 't:18.57' '\n' 'Pval.:0.000', bbox=props)
plt.xticks((0,1), ("2011", "2012"))
plt.xlabel('Years')
plt.title('Figure 6. Average rentals by Years.''\n')

# Comparar las rentas y weather conditión

#Compruebo la variable cuantitativa este bien sin ruido 
wbr.cnt.describe()
plt.hist (wbr.cnt)

#Comprobar que la variable cualitativa está bien y no tiene ruido
mytable = pd.crosstab(index=wbr["weathersit"], columns="count")
n=mytable.sum()
mytable2 = (mytable/n)*100
plt.bar(mytable2.index, mytable2['count'])

#Analisis de los tres grupos. Hacenos el subsetting
cnt_sunny=wbr.loc[wbr.weathersit==1, 'cnt']
cnt_cloudy=wbr.loc[wbr.weathersit==2, 'cnt']
cnt_rainy=wbr.loc[wbr.weathersit==3, 'cnt']


res=stats.f_oneway(cnt_sunny, cnt_cloudy,cnt_rainy)
print (res)
#print ("F:" round(res[0],3),"P.value", round(res[1],3))

wbr.cnt.describe()
# Al ser el p value menos a 0,005 rechazamos la hipotesis nula. Es decir, al menos dos de ellos son distintos
# La conclusion es que al menos grupos son distintos pero no se cuales. Hay varias formas de hacerlos

#Graphic comparison: confidence intervals for the means
plt.figure(figsize=(5,5))
ax = sns.pointplot(x="weathersit", y="cnt", data=wbr, capsize=0.05, ci=99.9, join=0) #ci=tengo un intervalo del confianzo del 99,9%
ax.set_ylabel('')
plt.yticks(np.arange(1000, 7000, step=500))
plt.ylim(800,6200)
plt.axhline(y=wbr.cnt.mean(), linewidth=1,
            linestyle= 'dashed',
            color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(1.5, 5000, 'Mean: 4504.3''\n''n: 731' '\n' 'F: 40.06''\n' 'Pval.: 0.000', bbox=props)
plt.xlabel('Weather Situation')
plt.title('Figure 8. Average rentals by Weather Situation.''\n')

#Hacer un boxplot para comparar
ax = sns.boxplot(x="weathersit", y="cnt", data=wbr)






