

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import pandas as pd        #gestionar dataframes
import numpy as np         #numeric python vectores
import matplotlib          #graficos estadisticos

name =['Yaling','Sofia','Maria','Pablo','Ines']
age = [28,23,25,23,25]

gender =['Female','Female','Female','Male','Female']

class2020 = pd.DataFrame({'name':name,'age':age, 'gender':gender})

del (age,gender,name)

class2020.shape   #Dimensiones del Dataframe
class2020.head(3) #Tres primeros
class2020.tail(2) #Dos ultimos

edad = class2020.age #Extraer  datos

del(edad)

#Get wprking directory
os.getcwd

#Cambiar el directorio de trabajo
os.chdir(r'C:/estadistica')
os.getcwd()

class2020.to_excel("class2020.xlsx")
class2020.to_csv("class2020.csv")