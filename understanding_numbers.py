# Números
# Enteros - Integers

"""
los números enteros los podemos
sumar, restar, multiplicar, dividir

"""
print(2+3)
print(3-2)
print(2*3)
print(3/2)
print(3**2)
print(10%2) #Módulo (mod)
age = 34
print(age)
name = "Wendy Lara"
print(name, age)

#Flotantes - floats
"""
     Python llama floats a cualquier 
     número con punto decimal
"""
print(0.1+0.1)
print(0.2-0.2)
print(2*0.1)
print(2*0.2)

# Imprimir la edad de alguien
age = 18 #Variable del tipo int
message = "Wendy tiene " + str(age) + " años."
print(message)
message_f = f"Wendy tiene {age} años"
print(message_f)

"""
   Typeerror: Python no puede reconocer el tipo
   de informacion que se esta utilizando.

   En este caso no se pueden concatenar
   ints a strings
"""
print(type(age))
print(type(message_f))
print(type(2+3), type(message_f))