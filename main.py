import modulo as mod
mod.saludar("Nadia")

#parametro "rt":accion:read-modo:text
archivo = open("ejemplo.txt", "rt")
datos = archivo.read()
archivo.close()

print(datos)

archivo2 = open("ejemplo2.txt", "wt")
texto = "Hola como están?!"
archivo2.write(texto)
archivo2.close()

archivo3 = open("ejemplo2.txt", "rt")
datos2 = archivo3.read()

print(datos2)




