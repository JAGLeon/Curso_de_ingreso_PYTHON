
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


""" 
Simulacro 01 - Dr. UTN

nombre: Anthony
apellido: Garay

Enunciado:

De 5 personas que ingresan al hospital se deben tomar y validar los siguientes datos.
    ● Nombre 
    ● Temperatura, entre 35 y 42
    ● Sexo( f, m , nb )
    ● Edad(mayor a 0)

Pedir datos por Prompt y mostrar por Print

Punto A - por el número de DNI del alumno:

DNI terminados en 0 o 1

1) Informar la cantidad de personas de sexo femenino
2) La edad promedio de personas de sexo masculino
3) El nombre de la persona la persona de sexo nb con más temperatura(si la hay)

DNI terminados en 2 o 3
1) Informar la cantidad de personas de sexo masculino
2) La edad promedio de personas de sexo nb
3) El nombre de la persona de sexo femenino con la temperatura mas baja(si la hay)

DNI terminados en 4 o 5
1) Informar la cantidad de personas de sexo nb
2) La edad promedio de personas de sexo femenino
3) El nombre de la persona la persona de sexo masculino con la temperatura mas baja(si la hay)

DNI terminados en 6 o 7
1) Informar la cantidad de personas mayores de edad (desde los 18 años)
2) La edad promedio en total de todas las personas mayores de edad (18 años)
3) El nombre de la persona la persona de sexo masculino con la temperatura mas baja(si la hay)

DNI terminados en 8 o 9
1) Informar la cantidad de personas menores de edad (menos de 18 años)
2) La temperatura promedio en total de todas las personas menores de edad
3) El nombre de la persona de sexo femenino con la temperatura mas baja(si la hay)
De 5 personas que ingresan al hospital se deben tomar y validar los siguientes datos.
    ● Nombre 
    ● Temperatura, entre 35 y 42
    ● Sexo( f, m , nb )
    ● Edad(mayor a 0)
Todos los alumnos:
B - Informar cual fue el sexo mas ingresado
C - El porcentaje de personas con fiebre y el porcentaje sin fiebre
"""


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=1, sticky="nsew")

    def btn_mostrar_on_click(self):
        cantidad_pacientes = 0
        contador_personas_mayores = 0
        suma_personas_mayores = 0
        cantidad_masculinos = 0
        cantidad_femeninos = 0
        cantidad_no_binario = 0
        contador_personas_con_fiebre = 0
        contador_personas_sin_fiebre = 0
        for cantidad_pacientes in range(1,6):
            nombre_ingresado= prompt("Ingrese","Nombre")

            temperatura_ingresado= prompt("Ingrese","Temperatura")
            temperatura_ingresado = int(temperatura_ingresado)
            while temperatura_ingresado < 35 or temperatura_ingresado > 42:
                temperatura_ingresado= prompt("Ingrese","Temperatura")
                temperatura_ingresado = int(temperatura_ingresado)

            sexo_ingresado= prompt("Ingrese","Sexo")
            while sexo_ingresado != "f" and sexo_ingresado != "m" and sexo_ingresado != "nb":
                sexo_ingresado= prompt("Ingrese","Sexo")

            edad_ingresado= prompt("Ingrese","Edad")
            edad_ingresado = int(edad_ingresado)
            while edad_ingresado < 1:
                edad_ingresado= prompt("Ingrese","Edad")
                edad_ingresado = int(edad_ingresado)

            if edad_ingresado > 17:
                contador_personas_mayores +=1
                suma_personas_mayores += edad_ingresado
            
            if temperatura_ingresado > 37:
                contador_personas_con_fiebre += 1
            else:
                contador_personas_sin_fiebre += 1

            match sexo_ingresado:
                case "m":
                    if cantidad_masculinos == 0:
                        nombre_masculino_temperatura_baja = nombre_ingresado
                        temperatura_mas_baja_masculino = temperatura_ingresado
                    else:
                        if temperatura_mas_baja_masculino > temperatura_ingresado:
                            temperatura_mas_baja_masculino = temperatura_ingresado
                            nombre_masculino_temperatura_baja = nombre_ingresado
                    cantidad_masculinos += 1
                case "f":
                    cantidad_femeninos += 1
                case _:
                    cantidad_no_binario += 1

            print(f"\nNombre = {nombre_ingresado}\nEdad = {edad_ingresado}\nTemperatura = {temperatura_ingresado}\nSexo = {sexo_ingresado}\n")

        promedio_personas_mayores = suma_personas_mayores / contador_personas_mayores
        if cantidad_femeninos > cantidad_no_binario and cantidad_femeninos > cantidad_masculinos:
            mensaje_sexo_mas_ingresado = f"femenino"
        elif cantidad_masculinos > cantidad_no_binario:
            mensaje_sexo_mas_ingresado = f"masculino"
        else:
            mensaje_sexo_mas_ingresado = f"no binario"

        if cantidad_masculinos == 0:
            mensaje_temperatura_baja = f"-"
        else:
            mensaje_temperatura_baja = f"{nombre_masculino_temperatura_baja}"
        porcetaje_personas_con_fiebre = (contador_personas_con_fiebre * 100) / cantidad_pacientes
        porcetaje_personas_sin_fiebre = (contador_personas_sin_fiebre * 100) / cantidad_pacientes
        
        print(f"Cantidad de personas mayores {contador_personas_mayores}\nLa edad promedio de todas las personas mayores es: {promedio_personas_mayores}\nEl nombre de la persona la persona de sexo masculino con la temperatura mas baja es : {mensaje_temperatura_baja}\nEl sexo mas ingresado es: {mensaje_sexo_mas_ingresado}\nEl porcentaje de personas con fiebre  es: {porcetaje_personas_con_fiebre}%\nEl porcentaje de personas sin fiebre  es: {porcetaje_personas_sin_fiebre}%")
# DNI terminados en 6 o 7
# 1) Informar la cantidad de personas mayores de edad (desde los 18 años)
# 2) La edad promedio en total de todas las personas mayores de edad (18 años)
# 3) El nombre de la persona la persona de sexo masculino con la temperatura mas baja(si la hay)
# Todos los alumnos:
# B - Informar cual fue el sexo mas ingresado
# C - El porcentaje de personas con fiebre y el porcentaje sin fiebre
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
