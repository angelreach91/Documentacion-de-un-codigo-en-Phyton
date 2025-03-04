#Equipo 1
#Trabajo Jose Maximiliano Hernandez Loeza
#Este código saolicita un numero y determina si es par o impar para despues mostrar en la pantalla ¨el numero es par¨ 0 ¨el numero es impar¨
numero = int(input("Ingrese un número: ")) #en esta linea se pide al usuario que ingrese cualquier numero¨

if numero % 2 == 0:#aqui realiza una operacion matematica (divide el numero entre 2) si el residuo es 0 pasa a la siguiente linea, si no lo es salta a la linea 8
    print("El número es par")#ejecuta el texto mostrandolo en la pantalla si la condicion de el residuo =0 se cumplio
else:#el codigo salta a esta linea si el residuo de la operacion fue diferente a 0
    print("El número es impar")#cuando el residuo fue diferente a 0 se ejecuta esta linea mostrando el texto en pantalla
