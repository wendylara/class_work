# if Statement
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == "audi": #if nos ayuda a hacer especificaciones
        print(car.upper())
    else:   # else lo acompaña para decir lo demas que no sea if
        print(car)

"""
   Este código nos quiere decir que si en la variable 'car'
   es igual a 'audi' se debera imprimir en mayusculas, mientras
   que el resto seguira igual. Asi lo mismo para el que pongamos
   en if.
"""

# Condicional o condition
# El condicional es el corazón del if

# Concicional verdadero
# Condicional = True
truck = 'ford'
print(truck == 'ford') # Doble igual, sirve para hacer comparaciones de verdadero/ falso
print(truck == 'chevrolet')
print(truck == 'Ford'.lower()) # Determina iguales

# Condicional falso
# Conditional false
print(truck == 'Audi')
print(truck == 'Ford')


# Condicional de desigualdad !=
print(truck!="audi") # Con este podemos ver su es diferente, de serlo nos dara un true
print(truck!="ford") # Aqui me dara un false porque es igualdad


# Comaparaciones numéricas
age = 18
print(age==18) # True
print(age==34) # False

answer = 17
if answer != 42:
    print("esa no es la respuesta correcta")

# Multiple conditions
age_0 = 22
age_1 = 18

# AND
print("Operación and".upper())
print(age_0>=21 and age_1>=21) # False, porque ambos son falsos
print(age_0>=21 and age_1>=18) # True, porque ambos son verdaderos

# OR
print("Operación or".upper())
print(age_0>=21 or age_1>=21) # True
print(age_0>=23 or age_1>=21) # False


# ¿Cómo saber si un elemento esta en una lista?
food = ['chilaquiles', 'flautas', 'gorditas', 'tamales']
print("¿nopales esta en la lista?")
print("nopales" in food)
print("¿gorditas esta en la lista?")
print("gorditas" in food)

# ¿Cómo saber si un elemento no esta en una lista?
banned_user = ['andrew', 'carolina', 'david']
user = "marie"
print(user not in banned_user)