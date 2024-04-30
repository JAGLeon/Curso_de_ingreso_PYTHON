
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
        contador_menores_edad = 0
        suma_temperatura_menores_edad = 0
        contador_sexo_femenino = 0
        contador_sexo_masculino = 0
        contador_sexo_no_binario = 0
        personas_con_fiebre = 0
        personas_sin_fiebre = 0

        for contador_personas in range(1,6):
            nombre_ingresado = prompt("Ingrese", "Nombre")

            temperatura_ingresado = prompt("Ingrese","Temperatura")
            temperatura_ingresado = int(temperatura_ingresado)
            while temperatura_ingresado < 35 or temperatura_ingresado > 42:
                temperatura_ingresado = prompt("Re-ingrese","Error temperatura debe ser entre 35 y 42")
                if temperatura_ingresado != None:
                    temperatura_ingresado = int(temperatura_ingresado)

            edad_ingresado = prompt("Ingrese","Edad")
            edad_ingresado = int(edad_ingresado)
            while edad_ingresado < 1:
                edad_ingresado = prompt("Re-ingrese","Error edad debe ser mayor a 0")
                edad_ingresado = int(edad_ingresado)

            sexo_ingresado = prompt("Ingrese", "Sexo")
            while sexo_ingresado != "f" and sexo_ingresado != "m" and sexo_ingresado != "nb":
                temperatura_ingresado = prompt("Re-ingrese","Error sexo debe ser f/m/nb")

            if edad_ingresado < 18:
                contador_menores_edad += 1
                suma_temperatura_menores_edad += temperatura_ingresado

            match sexo_ingresado:
                case "f":
                    if contador_sexo_femenino == 0:
                        femenina_temperatura_mas_baja = temperatura_ingresado
                        nombre_femenina_temperatura_mas_baja = nombre_ingresado 
                    else:
                        if femenina_temperatura_mas_baja > temperatura_ingresado:
                            femenina_temperatura_mas_baja = temperatura_ingresado 
                            nombre_femenina_temperatura_mas_baja = nombre_ingresado
                    contador_sexo_femenino +=1
                case "m":
                    contador_sexo_masculino +=1
                case _:
                    contador_sexo_no_binario +=1

            if temperatura_ingresado > 38:
                personas_con_fiebre += 1
            else:
                personas_sin_fiebre += 1

            print(f"Nombre = {nombre_ingresado}\nTemperatura = {temperatura_ingresado}\nEdad = {edad_ingresado}\nSexo = {sexo_ingresado}\n\n")


        if contador_sexo_femenino > contador_sexo_masculino and contador_sexo_femenino > contador_sexo_no_binario:
            mayor_ingreso_por_sexo = "femenino"
        elif contador_sexo_masculino > contador_sexo_no_binario:
            mayor_ingreso_por_sexo = "masculino"
        else:
            mayor_ingreso_por_sexo = "no binario"


        if contador_menores_edad > 0:
            mensaje_promedio_menores = f"Personas menores de edad: {contador_menores_edad}"
            if suma_temperatura_menores_edad > 0:
                promedio_temperatura_menores_edad = suma_temperatura_menores_edad / contador_menores_edad
                mensaje_temperatura_promedio_menores = f"Temperatura promedio de menores de edad: {promedio_temperatura_menores_edad}"
            else:
                mensaje_temperatura_promedio_menores = f"Temperatura promedio de menores de edad: -"
        else:        
            mensaje_promedio_menores = f"Personas menores de edad: -"

        if contador_sexo_femenino != 0:
            mensaje_nombre_sexo_femenino_temperatura_mas_baja= f"Sexo femenino de nombre con temperatura mas baja: {nombre_femenina_temperatura_mas_baja}"
        else:
            mensaje_nombre_sexo_femenino_temperatura_mas_baja= f"Sexo femenino de nombre con temperatura mas baja: -" 
         
        if personas_con_fiebre != 0:
            porcentaje_personas_con_fiebre = (contador_personas/personas_con_fiebre) * 100            
            mensaje_porcentaje_personas_con_fiebre = f"Porcentaje de personas con fiebre: {porcentaje_personas_con_fiebre}"
        else:
            mensaje_porcentaje_personas_con_fiebre = f"Porcentaje de personas con fiebre: -"

        if personas_sin_fiebre != 0:
            porcentaje_personas_sin_fiebre = (contador_personas/personas_sin_fiebre) * 100
            mensaje_porcentaje_personas_sin_fiebre = f"Porcentaje de personas sin fiebre: {porcentaje_personas_sin_fiebre}"
        else:
            mensaje_porcentaje_personas_sin_fiebre = f"Porcentaje de personas sin fiebre: -"

        print(f"{mensaje_promedio_menores}\n{mensaje_temperatura_promedio_menores}\n{mensaje_nombre_sexo_femenino_temperatura_mas_baja}\nMayor de ingreso por sexo: {mayor_ingreso_por_sexo}\n{mensaje_porcentaje_personas_con_fiebre}\n{mensaje_porcentaje_personas_sin_fiebre}")
     
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
