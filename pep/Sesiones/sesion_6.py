# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 19:48:26 2021

@author: Jose
"""
#plt.show() para cerrar los gráficos y que no vaya cambiando los colores


reset -f
#Para saber transformar los datos

import os                                 #Sistema Operativo
import pandas as pd                       #Gestionar Dataframes
import numpy as np                        #Numeric python vectores matrices
import matplotlib.pyplot as plt           # graficos

#Poner donde está ubicado
os.chdir(r'C:\Users\Jose\OneDrive\Escritorio\EDEM\GitKraken\Edem2021\pep\code_and_data')  #Define la carpeta de trabajo. Se tiene que hacer lo primero 
os.getcwd()

#Insertar el archivo
wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')

#comprobamos la dimensionalidad
wbr.shape

#crear una nueva columna que sea el número de casuales entre el número de registados

wbr['cs_ratio']=(wbr.casual)/(wbr.registered) #generamos una nueva columna en la que haya el numero de casuales entre el número de registrados

wbr.cs_ratio.describe()
plt.hist(wbr.cs_ratio)

#Calcular una variable 

#Borramos la variable cnt 

del(wbr['cnt'])

#Para recuperar la culumna sumamos casual y registrados
wbr['cnt'] =wbr.casual + wbr.registered

#RECODIFICAR UNA VARIABLE. La variable season 1 invierno 2 primavera 3 verano 4 otoño. Recodificamos creando una nueva variable y en función de estos valores creare una nueva variable tipo texto

wbr.loc[ (wbr['season']==1), "season_cat"]= "Winter" #vamos a generar una nueva columna que se llama season_cat en la cordenada y ( los primero fila y lo segundo columnos). Tiene que escribirlo en la nueva columna y en las filas que satisfagan la condicion las filas wbr
wbr.loc[(wbr['season']==2), "season_cat"]= "Spring"  # .loc es de localización
wbr.loc[(wbr['season']==3), "season_cat"]= "Summer"    
wbr.loc[(wbr['season']==4), "season_cat"]= "Autum"   

#Hacemos una tabla cruzada de variable original contra la nueva para comprobar que está bien hecha

pd.crosstab(wbr.season, wbr.season_cat)     
#QC OK

#Vamos a tranformar una variable númerica de verdad, para hacerla en categorias. Sabiendo los días si son bajas, altas o bajas. De variable númerica a ordinal
#Para decidir si un dia es malo podemos usar lo que queramos. Usamos los cuartiles. Otro punte la media menos la desviación y la media más la disviación

res = wbr['cnt'].describe()
print (res)

wbr.cnt.describe()
#Vamos a definir los puntos de corte
print('Low limit:', round(4504.348837-1937.211452,0))
print('Mean:', 4504.348837)
print('Upper limit:', round(4504.348837+1937.211452,0))

#Recodificamos la variable 

wbr.loc[ (wbr['cnt']<2567), "cnt_cat2"]= "1: Low rentals" #vamos a generar una nueva columna que se llama season_cat en la cordenada y ( los primero fila y lo segundo columnos). Tiene que escribirlo en la nueva columna y en las filas que satisfagan la condicion las filas wbr
wbr.loc[ ((wbr['cnt']>2567.1) & (wbr['cnt']<6442)) ,"cnt_cat2"]= "2: Average rentals"
wbr.loc[ (wbr['cnt']>=6442), "cnt_cat2"]= "3: Higs rentals"

#En el caso de una variable númerica, hacemos un scatter de la variable original contra la nueva 

plt.scatter(wbr.cnt, wbr.cnt_cat2, s=1)  #s = size   
#QC OK

#Vemos la variable nueva creada 

# Frecuencias

mytable = wbr.groupby(['cnt_cat2']).size()
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

# Creamos una nueva variable categorica pero sin 1,2 y 3. Cuando python hace una tabla utilzia el criterio alfabetico.

wbr.loc[ (wbr['cnt']<2567), "cnt_cat3"]= "Low rentals" #vamos a generar una nueva columna que se llama season_cat en la cordenada y ( los primero fila y lo segundo columnos). Tiene que escribirlo en la nueva columna y en las filas que satisfagan la condicion las filas wbr
wbr.loc[ ((wbr['cnt']>2567.1) & (wbr['cnt']<6442)) ,"cnt_cat3"]= "Average rentals"
wbr.loc[ (wbr['cnt']>=6442), "cnt_cat3"]= "High rentals"

#En el caso de una variable númerica, hacemos un scatter de la variable original contra la nueva 

plt.scatter(wbr.cnt, wbr.cnt_cat2, s=1)  #s = size   
#QC OK

mytable = wbr.groupby(['cnt_cat3']).size()
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

#VARIABLE ORDINAL(categorica)
#Las variables ordinales estan entre las cuantitativas y cualitativas. Se analizan con porcentajes y gráficos de barras, las barras tienen que estar ordenadas

wbr.dtypes  #para saber los tipos de datos que hay en las variables de mi tabla int64-números enteros, object-texto o mezcla con lo que sea, float64-número decimales, bool-lógicas, category

#tranformar mi variable rentals pase de ser una string a considerarlo una lista finita de categorias (malas, normales y buenas). Una vez sepa que es una variable categorica se puede ordenar
#Para poder definir la variable cat_3 como una variable categorica hay que importar lo siguiente

from pandas.api.types import CategoricalDtype

#Definir tipo de datos especifico para nuestra variable

#1º definir la lista de las categorias
my_categories=["Low rentals", "Average rentals", "High rentals"]

#2º Definir el nuevo tipo de dato. Generamos el nuevo tipo de dato
my_rentals_type = CategoricalDtype(categories=my_categories, ordered=True) #Estos datos es una variable categorica con la lista que hemos creado arriba y ademas decirle que la lista esta ordenada

#3º Vamos a forzar la variable. Generar la nueva columna que va ser las cat_3 forzandola a que sea una varibale categorica 
wbr["cnt_cat5"] = wbr.cnt_cat3.astype(my_rentals_type) 

#Reprensentar 
mytable = wbr.groupby(['cnt_cat5']).size()
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

#Comprobamos que haya cambiado
wbr.dtypes  #para saber los tipos de datos que hay en las variables de mi tabla int64-números enteros, object-texto o mezcla con lo que sea, float64-número decimales, bool-lógicas, category















