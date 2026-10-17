# Trabajando con listas
magicians = ['harry', 'ron', 'hermione']
print(magicians)

print(magicians[0], magicians[1], magicians[2])

# Como acceder a los elemenetos de una lista
# Ciclo for
for magician in magicians:
    print(magician)

# A esto se le conoce como looping

# Ahora vamos a imprimir un mensaje para cada mago

for magician in magicians:
    print(f"{magician.title()} ese fue un gran hechizo.")
    print(f"No puedo esperar a ver el siguiente hechizo, {magician.upper()}")
print("Gracias a todos, fue un gran espectaculo")

#for se usa para reducir codigos

# Identación
"""
Python utiliza la indentación para determinar
cuando la línea de código está concectada a la
línea de codigo anterior.

Basicamente, se utilizan 4 espacios en blanco para
obligarnos a escribir codigo ordenado y estructurado.
"""
# No olvidemos identar - Traceback IdentationError
magicians = ["alice", "david", "caroline"]
#for magician in magicians:
#    print(magician)

# Error de logica - Logic Error - IdentationError
for magician in magicians:
    print(magician)
print(f"No puedo esperar a ver el siguiente tuco, {magician}")


# Identation Inecesaria
message = "Hello python world"
#    print(message)

# No olvidar los dos puntos - Syntax Error
#for magician in magicians
#    print(magician)