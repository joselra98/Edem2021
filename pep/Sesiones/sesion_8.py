# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 18:19:24 2021

@author: Jose
"""

#Resets ALL (Careful This is a "magic" function then it doesn't run as script) 
#reset -f   

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


#Recoding DV for analysis
res = wbr.cnt.describe()
print (res)
# Store parameters as numbers
m  = res[1]
sd = res[2]
n  = res[0]

### Recode cnt to string
wbr.loc[  (wbr['cnt']<(m-sd)) ,"cnt_str"]= "Low rentals"
wbr.loc[ ((wbr['cnt']>(m-sd)) & (wbr['cnt']<(m+sd))) ,"cnt_str"]= "Average rentals"
wbr.loc[  (wbr['cnt']>(m+sd)) ,"cnt_str"]= "High rentals"

### Recode cnt to ordinal
my_categories=["Low rentals", "Average rentals", "High rentals"]
my_rentals_type = CategoricalDtype(categories=my_categories, ordered=True)
wbr["cnt_cat"] = wbr.cnt_str.astype(my_rentals_type)
wbr.info()

#frequencies & barchart
mytable = pd.crosstab(wbr.cnt_cat, columns="count", normalize='columns')*100
print(mytable)
print (round(mytable,1))
plt.bar(mytable.index, mytable['count'])

#######################
# Recode  working day
# To string
wbr["wd_st"] = wbr.workingday
wbr.wd_st = wbr.wd_st.replace(to_replace=0, value="No")
wbr.wd_st = wbr.wd_st.replace(to_replace=1, value="Yes")
#To category
my_categories=["No","Yes"]
my_datatype = CategoricalDtype(categories=my_categories, ordered=True)
wbr["wd_cat"] = wbr.wd_st.astype(my_datatype)
wbr.info()

# Barchart for Working day
mytable = pd.crosstab(index=wbr["wd_cat"], columns="count") # Crosstab
n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)
plt.bar(mytable2.index, mytable2['count'])
plt.xlabel('Working Day')
plt.title('Figure 5. Percentage of Working Days')

#Tablas cruzadas
# Paso uno confimar que cuando montamos la variable de contigencia mi última columna sea la distribución de la cariable dependiente y que el resto de columnas smen 100

#Hacemos la primera versión de la tabla cruzada
pd.crosstab(wbr.cnt_cat,wbr.wd_cat, margins= True) #Primero la variable dependiente, segundo la variable predictora o independiente
#Me dice que tengo 42 dias no laborables que vendo mucho

#Segunda version de la tabla cruzada
pd.crosstab(wbr.cnt_cat,wbr.wd_cat, normalize='columns', margins=True)*100
#me dice lo de arriba pero con porcentages

#Redondeamos la tabla cruzada, para ello lo guardo en un objeto
my_ct= pd.crosstab(wbr.cnt_cat,wbr.wd_cat, normalize='columns', margins=True)*100 #el total es el margins=true frecuencias marginales
my_ct

round(my_ct, 1) #El 1 es a cantidad de decimales Funciones
my_ct.round(1) #Otra forma de redondear, se autoredondea. Objeto.Metodo

#La tabla redondeada 
my_ct = round (my_ct, 1)
my_ct

#Quiero poder saber si las diferencias entre los porcntajes son significativas o no 

#Para ello hago otra tabla cruzada que no tenga la última columna. para calcular chi2
ct= pd.crosstab(wbr.cnt_cat, wbr.wd_cat)
ct

#Liberia
import scipy.stats as stats

#Calculamos el valor de chi2 (4.98) y el nivel de significacion y el pvalue(0.08). Para nosotros el working day no importa en las ventas
stats.chi2_contingency(ct)

#Hacemos el gráfico
my_ct.plot ( kind="bar") #Confunde filas por columnas 


#Para arreglarlo vamos a trasponer la tabla
my_ct2=my_ct.transpose()

#Represento el gráfico
my_ct2.plot(kind="bar")

my_ct2.plot(kind="bar", edgecolor="black")


#Mapa de colores 
my_ct2.plot(kind="bar", edgecolor = "black", colormap='Blues')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(-0.4, 81, 'Chi2: 4983''\n''n: 731' '\n' 'Pval.: 0.083', bbox=props)
plt.xlabel('Working Day')
plt.title('Figure 7. Percentage of Rental level, by Working Day.''\n')
plt.legend(['Low rentals','Average rentals','High rentals'])
plt.ylim(0,100)
plt.xticks(rotation='horizontal')

#La guardo para llevarmela al powerpoint
plt.savefig('cross_tab_plot2.eps')

#Ejercicio hacer lo mismo que arriba con weather_sit. Decir si en las distitas weather_sit el porcentage de ventas cambia
#Primero hay que pasarla ordinal 
reset -f
# Recode  working day
# To string
wbr["wd_st"] = wbr.weathersit
wbr.wd_st = wbr.wd_st.replace(to_replace=1, value="Sunny")
wbr.wd_st = wbr.wd_st.replace(to_replace=2, value="Cloudy")
wbr.wd_st = wbr.wd_st.replace(to_replace=3, value="Rainy")

#To category
my_categories=["Sunny","Cloudy","Rainy"]
my_datatype = CategoricalDtype(categories=my_categories, ordered=True)
wbr["wd_cat"] = wbr.wd_st.astype(my_datatype)
wbr.info()

# Barchart for Working day
mytable = pd.crosstab(index=wbr["wd_cat"], columns="count") # Crosstab
n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)
plt.bar(mytable2.index, mytable2['count'])
plt.xlabel('Working Day')
plt.title('Figure 5. Percentage of Working Days')

#Hacemos la primera versión de la tabla cruzada
pd.crosstab(wbr.cnt_cat,wbr.wd_cat, margins= True) #Primero la variable dependiente, segundo la variable predictora o independiente
#Me dice que tengo 42 dias no laborables que vendo mucho

#Segunda version de la tabla cruzada
pd.crosstab(wbr.cnt_cat,wbr.wd_cat, normalize='columns', margins=True)*100
#me dice lo de arriba pero con porcentages

#Redondeamos la tabla cruzada, para ello lo guardo en un objeto
my_ct= pd.crosstab(wbr.cnt_cat,wbr.wd_cat, normalize='columns', margins=True)*100 #el total es el margins=true frecuencias marginales
my_ct

round(my_ct, 1) #El 1 es a cantidad de decimales Funciones
my_ct.round(1) #Otra forma de redondear, se autoredondea. Objeto.Metodo

#La tabla redondeada 
my_ct = round (my_ct, 1)
my_ct

#Quiero poder saber si las diferencias entre los porcntajes son significativas o no 

#Para ello hago otra tabla cruzada que no tenga la última columna. para calcular chi2
ct= pd.crosstab(wbr.cnt_cat, wbr.wd_cat)
ct

#Calculamos el valor de chi2 (68.76) y el nivel de significacion y el pvalue(4.13-14). Para nosotros el wathersit si que afecta en las ventas
stats.chi2_contingency(ct)

#Hacemos el gráfico
my_ct.plot ( kind="bar") #Confunde filas por columnas 


#Para arreglarlo vamos a trasponer la tabla
my_ct2=my_ct.transpose()

#Represento el gráfico
my_ct2.plot(kind="bar")

my_ct2.plot(kind="bar", edgecolor="black")


#Mapa de colores 
my_ct2.plot(kind="bar", edgecolor = "black", colormap='Blues')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(-0.4, 81, 'Chi2: 6876''\n''n: 731' '\n' 'Pval.: 0.000', bbox=props)
plt.xlabel('Weather Situation')
plt.title('Figure 7. Percentage of Rental level, by Weather Situation.''\n')
plt.legend(['Sunny','Cloudy','Rainy'])
plt.ylim(0,100)
plt.xticks(rotation='horizontal')




























































