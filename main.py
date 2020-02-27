import modulo as mod
#mod.saludar("Nadia")

#parametro "rt":accion:read-modo:text
archivo = open("ejemplo.txt", "rt")
datos = archivo.read()
archivo.close()

#print(datos)

archivo2 = open("ejemplo2.txt", "wt")
texto = "Hola como están?!"
archivo2.write(texto)
archivo2.close()

# "at" = append text
archivo2 = open("ejemplo.txt", "at")
texto2 = "\n texto a incluir 2"
archivo2.write(texto2)
archivo2.close()

archivo2 = open("ejemplo2.txt", "rt")
datos2 = archivo2.read()

#print(datos2)

#clase 4, manejo de errores
num1 = 5
num2 = 0

#try:
  #div = num1 / num2
  #print(div)
#except: 
  #print("Error, no se puede dividir por 0")  

#try:
  #div = num1 / num2

#except Exception as e:
  #print(e)
#else: 
  #print("no hay errores")
#finally:
  #print("resultado:" + str(div))  


#texto = "texto para cambiar"

#import re

#print(texto)
#resultado = re.sub("para cambiar","cambiado", texto)
#print(resultado)

#import json

#producto = {"item": "001", "color": "rojo", "valor": "1200"}

#prodjson = json.dumps(producto)
#print(prodjson)

#proddicc = json.loads(prodjson)
#print(proddicc["valor"])

from datetime import datetime

fyh = datetime.now()
#print(fyh)

#print("año:", fyh.year)
#print("mes:", fyh.month)
#print("día:", fyh.day)

#print("hora:", fyh.hour)
#print("minutos:", fyh.minute)
#print("segundo:", fyh.second)


import sqlite3

conexion = sqlite3.connect("datos.db")
cursor = conexion.cursor()

cursor.execute("UPDATE personas SET edad = 30 where nombre = 'Luis'")  

conexion.commit()  
conexion.close()












