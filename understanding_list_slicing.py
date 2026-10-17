players = ["charly", "juan", "iancarlo", 'lisandro']
print("Lista original: ", players)

# Slicing
print(players[0:2]) # ["charly", "juan"]

# El slicing nos permite trabajar con un grupo
# especifico de una lista: al resultado se le conoce como
# "un slice".

print(players[1:4]) # Imprime de 'A' a 'B'
print(players[:4]) # Imprime desde el inicio de lista hasta donde marque
print(players[0]) # Imprime solo un elemento seleccionado
print(players[2:]) # Imprime desde lo marcado hasta el final de lista
print(players[-3:])

# Casos especiales
print(players[1:6]) # No lo marca como error
print(players[6:1]) # Da una lista vacia porque no existe el indice buscado
print(players[:0]) # DA lista vacia porque no hay elementos de inicio

# Looping through a slice
students = ["charly", "juan", "iancarlo", 'lisandro']
for student in students[:4]:
    print(f"El estudiante {student}, va a pasar la materia")

"""
  Con el slice solo obtengo algunos elementos de la lista
  añadiendole un mensaje independiente a cada uno.
"""

# ¿Cómo podemos copiar una lista?
my_food = ['pizza', 'tacos', 'flautas']
my_friend_food = my_food # Manera erronea de copiar una lista

# Tres maneras de copiar una lista
# metodo 1 - utilizando slicing
my_friend_food_2 = my_food[:]
# metodo 2 - utilizando el metodo .copy()
my_friend_food_3 = my_food.copy()
# Metodo 3 - utilizando el metodo build-in list()
my_friend_food_4 = list(my_food)