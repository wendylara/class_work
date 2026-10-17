# if statement
"""
if condition:
   do something
"""
# Condicion verdadera se imprimira mensaje
age = 18
if age >= 18:
    print("Tu tienes la edad para votar")
    print("¿YA fuiste a tramitar tu INE?")

# Condicion falsa no se imprimira nada
age = 17
if age >= 18:
    print("Tu tienes la edad para votar")
    print("¿YA fuiste a tramitar tu INE?")

# De este modo mostraras un mensaje aunque sea falso
age = 17
if age >= 18:
    print("Tu tienes la edad para votar")
    print("¿YA fuiste a tramitar tu INE?")
else:
    print("Lo siento, eres demasiado joven para votar")
    print("Ve a registrarte cuando cumplas 18 años")
