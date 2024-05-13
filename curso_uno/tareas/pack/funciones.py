def validar_e_ingresar_numero()-> int:
    numero = input("Ingrese un numero : ")
    while not numero.isdigit():
        numero = input("ERROR re-ingrese un numero : ")
    return int(numero)

def suma(valor_uno: int, valor_dos: int)-> int:
    return valor_uno + valor_dos

def resta(valor_uno: int, valor_dos: int)-> int:
    return valor_uno - valor_dos

def dividir(valor_uno: int, valor_dos: int)-> float:
    return valor_uno / valor_dos

def multiplicar(valor_uno: int, valor_dos: int)-> int:
    return valor_uno * valor_dos

def menuOperaciones():
    print('''\n1- Sumar
2- Restar
3- Dividir
4- Multiplicar\n''')
    return

def whileOpciones(valor_uno: int, valor_dos: int):
    while True:
        opcion = input("\nIngrese un opcion : \n")
        match opcion.lower():
            case "sumar" | "1":
                return suma(valor_uno,valor_dos)
            case "restar" | "2":
                return resta(valor_uno,valor_dos)
            case "dividir" | "3":
                if valor_dos == 0:
                    print("No se puede dividir por 0")
                else:
                    return dividir(valor_uno,valor_dos)
            case "multiplicar" | "4":
                return multiplicar(valor_uno,valor_dos)


