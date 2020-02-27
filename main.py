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


texto = """texto de ejemplo para buscar
otro texto
otro texto mas
más texto
y el último
"""

import re

resultado = re.findall("texto", texto)
if(resultado):
  print("palabra encontrada " + str(len(resultado)) + " veces")
else:
  print("texto no encontrado")  








