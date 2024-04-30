dni = input("Ingrese su dni: ")
edad = input("Ingrese su edad: ")
def ingreso_de_datos(dni,edad):
    """ Ingreso de datos
        Args:
            edad (int),dni (int): una vez validados
        Return:
            int
    """
    while not dni.isdigit() or len(dni) != 8:
        dni = input("Ingrese un DNI numero con 8 digitos: ")

    while not edad.isdigit() or (edad.isdigit() and int(edad) < 17) :
        edad = input("Debe ingresar una edad valida y mayor a 16: ")

    return(int(dni),int(edad))

print(ingreso_de_datos(dni,edad))
