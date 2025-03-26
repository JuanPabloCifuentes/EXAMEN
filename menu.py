import json

file =  open("archivo.json") 
users = json.load(file)


#for user in users:
    #print("nombre de artista", user["Artist name"], ", musica:", user["Country"])
#file.close()

menu_principal = """
******Bienvenido quedea hacer******
Que sea hacer?
1.Registar de artistas
2.Gestion por Paises
3.Gestion por Gener Musical
4.Generar Informe
5.Modulo de Reportes
6.Para salir 
"""


def mostrar_principal():
 print(menu_principal)

 def pedir_opc_menu():
    return input ("Ingrese la Opcion: ")

def ejecucion_pricipal():
    while True:
        mostrar_principal() 
        opc = pedir_opc_menu()
        if opc == "1":
            print("registar cliente")
        elif opc == "2":
            print ("gestion por paises")
        elif opc == "3":
            print ("Gestion por Genero mucisical")
        elif opc == "4":
            print("generar informe")
        elif opc== "5":
            print("modulo de resportes")
        elif opc == "6":
            print("Saliendo...")
            break
        else: 
            print("lea Bien Pedejo...")                     