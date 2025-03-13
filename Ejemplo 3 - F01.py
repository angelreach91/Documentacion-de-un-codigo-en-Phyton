#Equipo 1
#Trabajo Jose Maximiliano Hernandez Loeza
#Este código solicita un numero y determina si es par o impar para despues mostrar en la pantalla ¨el numero es par¨ 0 ¨el numero es impar¨
try:                                             # El código dentro de try se ejecutará normalmente, pero si ocurre un error, el programa no se detendrá bruscamente, sino que saltará al bloque except.
numero = int(input("Ingrese un número: "))       # En esta linea se pide al usuario que ingrese cualquier numero¨

if numero % 2 == 0:                              # Aqui realiza una operacion matematica (divide el numero entre 2) si el residuo es 0 pasa a la siguiente linea, si no lo es salta a la linea 8
    print("El número es par")                    # Ejecuta el texto mostrandolo en la pantalla si la condicion de el residuo =0 se cumplio
else:                                            # El codigo salta a esta linea si el residuo de la operacion fue diferente a 0
    print("El número es impar")                  # Cuando el residuo fue diferente a 0 se ejecuta esta linea mostrando el texto en pantalla
#Trabajo de José Julián Córdoba Martínez
except ValueError: #Captura si se ha ingresado algún dato o caracter que no sea un número como letras o símbolos
    print("Error: Debe ingresar un número válido.") #Si se detecta que no es un número, envía este mensaje.
