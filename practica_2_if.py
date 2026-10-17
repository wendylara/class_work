"""
    Ejercicio

    Realizar un programa que determine el costo
    de un boleto a partir de las siguientes condiciones:

    - costo para persona menor o igual a 4 años: gratis
    - costo para una persona cuya edad es mayor a 4
      años pero menor o igual a 18: $200
    - costo para una persona cuya edad es mayor a 18: $500

"""
age = input(" Ingresa tu edad: ")
#print(type(age)) #str
age = int(age)
#print(type(age)) #int


if age <=4:
    cost = 0

if age > 4 and age < 18:
    cost = 200

if age >= 18 and age < 65:
    cost = 500
if age >= 65:
    cost = 0

print(f"el costo de tu boleto es: {cost}")

# if-elif-else
print("\n uso de if-elif-else".upper())

if age <=4:
    cost = 0

elif age > 4 and age < 18:
    cost = 200

elif age >= 18 and age < 65:
    cost = 500

elif age >= 65:
    cost = 0

print(f"costo (if-elif-else): {cost}")