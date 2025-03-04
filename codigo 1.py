#Equipo 1 
# Trabajó Angel Jesus Libreros Ponce
numero1 = 5 #En est
numero2 = 3

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# validación para evitar división por cero
if numero2 == 0:
    print("Error: División por cero no es permitida.")
else:
    division = numero1 / numero2
    print("División:", division)

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
