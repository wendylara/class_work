# Listas de números
"""
   Las listas tambien pueden almacenar números. Python
   ofrece varias herramientas que ayudan a trabajar
   eficientemente con listas de números.
"""
# Método build- range()
"""
   El método range() nos ayuda a crear facilmente
   series de números.

   Ejemplo
"""

for value in range(1,6):
    print(value)

# Crear una lista de números utilizando range
numbers = list(range(1,6))
print(numbers)

# Lista de números pares
even_numbers = list(range(0,11,2))
print(even_numbers)

# Tarea: ¿Qué pasa con un paso negativo? range(5,1,2)

