# Agregando elementos a una lista
'''
motorcycles = ['honda', 'mortalika', 'yamaha']
print(motorcycles)

# Metodo append - agrega elementos a la lista
motorcycles.append('Kawasaki')
print(motorcycles)

"""
    Se utiliza para aregar
    elementos al final de 
    la lista.
"""

motorcycles_2 = [] # Lista vacia
print(motorcycles_2)

motorcycle = "ducati"
motorcycles_2.append(motorcycle)
motorcycles_2.append("yamaha")
motorcycles_2.append("suzuki")
print(motorcycles_2)
motorcycle = "Wendy"
print(motorcycles_2)
motorcycles_2.append(motorcycle)

# El método insert nos ayuda a agregar elementos
# a una lista en un índice específico
motorcycles_3 = ["honda", "yamaha", "suzuki"]
motorcycles_3.insert(0, "ducati")
print("\nLista original")
print(motorcycles_3)
motorcycles_3.insert(0, 'ducati')
print("Lista después del método insert")
print(motorcycles_3)

'''

# Método .pop() Elimina el último elemento de una lista
# pero nos permite utilizar el elemento después de eliminarlo.
motorcycles_4 = ['honda', 'suzuki', 'hd', 'mortalica']
print(motorcycles_4)
deleted_motorcycle = motorcycles_4.pop()
print(f"Tu motocicleta borrada es: {deleted_motorcycle}")
print(motorcycles_4)

# Se puede utilzar tambien para eliminar un elemento especifico
motorcycles_5 = ['honda', 'suzuki', 'hd', 'mortalica']
motorcycles_5.pop(0)
print(motorcycles_5) # Lista sin honda

# Método .remove(), permite eliminar elementos por su valor.
print("\n\t aqui aprendí a utilizar el método .remove()".upper())
motorcycles_6 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles_6)
motorcycles_6.remove("yamaha")
print(motorcycles_6)

# Ordenar listas
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort() # Ordenar las listas de manera permanente
print(cars)

# Argumento opcional de sort (reverse=True)
several_items = [["Wendy", "Joselin"], ["Subaru", "tsuru"]]
print (several_items[1][1])