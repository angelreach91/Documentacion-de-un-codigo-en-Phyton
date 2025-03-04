#Equipo 1 
# Trabajó Angel Jesus Libreros Ponce
#Se agregaron comentarios en cada linea 3/03/2025
#Este codigo realiza operacion aritmeticas básicas mediante dos numeros predefinidos, de igual forma se altero un poco el codigo añadiendo un if
# ya que las divisiones por cero no están permitidas ya que es un error matematico.
numero1 = 5 #En esta linea se define el primer numero con el que queremos realizar la operación
numero2 = 3 #En esta segunda linea se define el segundo digito con el que trabajaremos

suma = numero1 + numero2 #En esta linea se realiza una suma de los dos numeros dados en la linea 6 y 7 respectivamente
resta = numero1 - numero2 #En esta linea se realiza una resta de los dos numeros dados en la linea 6 y 7
multiplicacion = numero1 * numero2 #En esta linea se realizará una multiplicación

# validación para evitar división por cero
if numero2 == 0: #Este if revisara si el segundo numero es un 0 para así evitarla y mandar un mensaje en su defecto
    print("Error: División por cero no es permitida.") #Aquí se imprimira el mensaje en dado caso de que el segundo numero sea 0.
else: #El else nos servirá para dar a entender al lenguaje de programación que mientras no sea cero, cualquier otro numero será valido y se realizará la operación
    division = numero1 / numero2 #En esta linea se realizará la division de los numeros dados en la linea 6 y 7
    #A partir de esta linea se comenzaran a imprimir los resultados de dichas operaciones realizadas con anterioridad.
    print("División:", division) #Imprimiremos el resultado de la division
print("Suma:", suma) #Imprimiremos la suma
print("Resta:", resta) #Imprimiremos la resta
print("Multiplicación:", multiplicacion) #Imprimiremos la multiplicacion
