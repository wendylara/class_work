"""
   Crear una lista con
   los primeros 10 números cuadráticos.
"""

squares = []
for value in range(0,11):
    squares.append(value**2)
print(squares)

"""
Se genero una lisat vacias, despues con range para dterminar
de que numero a que nmero se haria el trabajo. Posterior con
.append pusimos que se elevara al caurado en value, mientras no
se cambie se repetira la accion las vees necesarias para al final
solo imprimir
"""