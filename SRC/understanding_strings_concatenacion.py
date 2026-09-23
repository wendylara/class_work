# Combinacion o Concatenacion de STRING
first_name = "wendy"
last_name = "lara"
full_name = first_name + " " + last_name
print(full_name.title())

print("Hola", "Wendy" + " " + "Camacho", first_name.title()+ " "+last_name.title())

message = "¡Hola, " + full_name.title() + "!"
print(message)


# WhiteSpace
"""
WhiteSpace se refiere a cualquier String
(caracter) que no se imprime, es decir,
un espacio (" "), tabuladores (\t) y
finales de linea (\n)

Los WhiteSpace se utilizan comunmente para
organizar las salidas de texto a usuario
de tal manera uqe sea mas amigable de leer
o ver para los usuarios.

"""
print("Python")
print("\tPython")
print("\t\tPython")
print("Lenguajes:\n\tPython\n\tC\nJavaScript")

# f-strings
famous_person = "wendy lara"
message = f"{famous_person} una vez dijo: Python es amor"
print(message)