from os import system  

def limpiar_pantalla():  
    system("cls")  

def pausar():  
    system("pause")  

def menu()->str:  
    limpiar_pantalla()  
    print(" Menu de opciones")  
    print("1- Saludar")  
    print("2- Brindar")  
    print("3- Despedir")  
    print("4- Salir")  
    return input("Ingrese opcion: ")

def saludar():  
    print("Hola. Que tal...")

def brindar():  
    print("Chin chin...")  

def despedir():  
    print("Chau. Nos vemos...")

bandera_saludar = False
bandera_brindar = False
bandera_despedir = False

while True:
    match menu() : 
        case "1":  
            saludar ()  
            bandera_saludar = True  
        case "2":  
            if bandera_saludar:  
                brindar ()  
                bandera_brindar = True  
            else:  
                print("Antes de brindar hay que saludar!")  
        case "3" :
            if not(bandera_saludar and bandera_brindar):  
                print("Antes de despedirse hay que saludar y brindar!")  
            elif bandera_saludar and not bandera_brindar:  
                print("Antes de despedirse hay que brindar!")  
            else:  
                despedir()  
                bandera_saludar = False
                bandera_brindar = False
                bandera_despedir = True  
        case "4":  
                break
    pausar()

print("Fin del programa")
