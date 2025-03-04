#Equipo1 
#Trabajo Maria Fernanda Rivera Vega 
#03 de Marzo del 2025 
#Este codigo nos imprira una lista de frutas que vayamos agregando 

frutas = ["manzana", "plátano", "naranja"] #Definimos una lista llamda frutas que contiene los elementos manzana, platano y naranja. 


frutas.append("pera") #El comando append agraga datos a la lista, en este caso pera 


print("Lista de frutas:", frutas) #Esta linea nos manda a imprimir la frase Lista de frutas y la fruta.


for fruta in frutas: #empezamos un bucle para recorrer un elemento
    print("Tengo una", fruta) #Nos imprime el texto Tengo una mas la fruta 
    #El bucle aun se imprime cuando la lista se modifique 
