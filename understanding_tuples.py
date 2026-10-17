"""
   TUPLAS
   Las tuplas son listas de elementos que no cambian de tamaño.
   Las tuplas son listas inmutables

   Se utilizan parentesis () para definir una tupla.

   Ejemplo:
       
       Si tenemos n rectangulo (largo, ancho) que siempre va
       a tener cierto tamaño, podemos asegurar que sus dimensiones
       no van a cambiar si colocamos sus valores en una tupla.
"""
dimensions = (200, 50) 
print(dimensions)

# Impresion de elementos de una tupla
# Se hace de la misma forma que con una lista
print(dimensions[0])
print(dimensions[1]) # De esta forma accedemos a los elementos de na tupla

# Modificar los elementos de una lista
names = ['carlos', 'charly', 'juan', 'wendy']
print(names)
names[0] = 'mercury'
print(names)


# dimensions[0] = 500 Esta acción en las tuplas no esta permitida

# Looping throgh a tuple
for dimension in dimensions:
    print(dimension)


"""
    No podemos modificar una tupla,
    lo que si podemos hacer es cambiar
    la asignación de una variable que 
    almacena una tupla.
"""
dimensions = (500, 1000) # Esto esta permitidio, ya que solo damos un valor nuevo 
print(dimensions) # Tupla reasignadas





"""
dir()
Asi conoces los métodos y atributos de la variable usada

print(dir(dimensions)) 

# Lista
dimensions_2 = [200, 50]
print(dir(dimensions_2))

# String
name = 'Wendy'
print(dir(name))

"""


# Tipos de datos booleanos
answer = True
print(answer)
# print(dir(answer))