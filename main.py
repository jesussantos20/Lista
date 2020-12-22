lista_articulos = list()
 
#funcion para agregar articulos a nuestra listaa
def agregar_articulos():
    print()
    print("Favor de agregar tus artículos")
    print()
    articulos = input("Agrega tu articulo: ")
    #Utilizamos string.capitaliza() para convertir nuestra primera letra en mayuscula
    lista_articulos.append(articulos.capitalize())
    print("Articulo agregados")
    print()
 
#Funcion para borrar elementos de nuestra lista
def borrar_articulos():
    articulo = input("Elementos a eliminar: ")
    #Agregamos de nuevo string.capitaliza()para que python no marque error
    lista_articulos.remove(articulo.capitalize())
    print("El articulo se ha borrado con exito!")
 
 
#Funcion para imprimir los artculos de nuestra lista
def ver_lista():
    #muestra los articulos en forma de lista de python
    #print(lista_articulos)
    print()
    print("Articulos en tu lista")
    print("------------")
    for articulos in lista_articulos:
        print("------------")
        print(articulos)
        print("------------")
    print("------------")
    print("Estos son tus articulos")
    print()
 
 
while  True:
    try:
        print("Menú")
        print ("1.- nombre")
        print ("2.- Borrar nombre")
        print ("3.- Ver toda las lista de los nombre")
        print ("4.- Salir")
 
        opcion = int(input("poner los nombre: "))
    except ValueError:
        print("Favor de ingresar una opcion valida")
    else:
        #si no es ninguna de las 4 opciones validas
        if opcion < 0 or opcion >4:
                print ("no es una opcion valida")
                continue
        if opcion == 1:
            agregar_articulos()
        elif opcion == 2:
            borrar_articulos()
        elif opcion == 3:
            ver_lista()
        else:
            break
print("Gracias por su participacion")