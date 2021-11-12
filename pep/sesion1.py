# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 16:55:05 2021

@author: Jose
"""


import os                                 #Sistema Operativo
import pandas as pd                       #Gestionar Dataframes
import numpy as np                        #Numeric python vectores matrices
import matplotlib.pyplot as plt           # graficos

# Crear la variables 

name =['Yaling','Sofia','Maria','Pablo','Ines']
age = [28,23,25,23,25]
gender =['Female','Female','Female','Male','Female']

#crear un dateframe

class2020 = pd.DataFrame({'name':name,'age':age, 'gender':gender})

#Borrar las variables 

del (age,gender,name)

#Validad el código

class2020.shape   #Dimensiones del Dataframe
class2020.head(3) #Tres primeros
class2020.tail(2) #Dos ultimos

#Quality Control OK

edad = class2020.age #Extraer  datos. Extraemos la variable edad del objeto class2020 y la metemos en la variable edad

del(edad)

#Get wprking directory
os.getcwd  #mirar donde se ha guardado

#Cambiar el directorio de trabajo
os.chdir(r'C:\Users\Jose\OneDrive\Escritorio\EDEM\GitKraken\Edem2021\pep')  #Elegir el directorio donde se guarda
os.getcwd()

# Guardamos en excel 

class2020.to_excel("class2020.xlsx")  
class2020.to_csv("class2020.csv")