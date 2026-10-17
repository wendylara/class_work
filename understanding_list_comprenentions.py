"""
Una list comprehension combina 
el for loop y la creacion de nuevos elementos
en una sola linea y atumaticamente agrega
cada nuevo elemeneto a la lista, es decir,
sin utilizar el metodo .append
"""
squares = [value**2 for value in range(0,11)]
print(squares)