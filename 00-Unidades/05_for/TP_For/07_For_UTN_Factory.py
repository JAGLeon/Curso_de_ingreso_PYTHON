import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Anthony
apellido:Garay
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

# Informar por pantalla:
# a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
# cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
# b. Nombre del postulante Jr con menor edad.
# c. Promedio de edades por género.
# d. Tecnologia con mas postulantes (solo hay una).
# e. Porcentaje de postulantes de cada genero.

# Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        cantidad_no_binario = 0
        suma_edad_m = 0
        suma_edad_f = 0
        suma_edad_nb = 0
        contador_masculino = 0
        contador_femenino = 0
        contador_no_binario = 0
        contador_python = 0
        contador_js = 0
        contador_net = 0

        for contador_ingresantes in range(10):
            nombre_ingresado = prompt("Ingrese","Nombre")

            edad_ingresado = prompt("Ingrese","Edad")
            edad_ingresado = int(edad_ingresado)
            while edad_ingresado < 18:
                edad_ingresado = prompt("Re-ngrese","Debe ser mayor de edad")
                edad_ingresado = int(edad_ingresado)

            genero_ingresado = prompt("Ingrese","Género F/M/NB")
            genero_ingresado = genero_ingresado.upper()
            while genero_ingresado != "F" and genero_ingresado != "M" and genero_ingresado != "NB":
                genero_ingresado = prompt("Re-ingrese","Género erroneo debe ser F/M/NB")
                genero_ingresado = genero_ingresado.upper()

            tecnologia_ingresado = prompt("Ingrese","Tecnología")
            tecnologia_ingresado = tecnologia_ingresado.upper()
            while tecnologia_ingresado != "PYTHON" and tecnologia_ingresado != "JS" and tecnologia_ingresado != "ASP.NET":
                tecnologia_ingresado = prompt("Re-ingrese","Tecnología errada debe ser PYTHON/JS/ASP.NET")
                tecnologia_ingresado = tecnologia_ingresado.upper()

            puesto_ingresado = prompt("Ingrese","Puesto")
            puesto_ingresado = puesto_ingresado.upper()
            while puesto_ingresado != "JR" and puesto_ingresado != "SSR" and puesto_ingresado != "SR":
                puesto_ingresado = prompt("Ingrese","Puesto")
                puesto_ingresado = puesto_ingresado.upper()

            if contador_ingresantes == 0 and puesto_ingresado == "JR":
                postulante_edad_menor = edad_ingresado
                postulante_nombre_menor_jr = nombre_ingresado
            elif puesto_ingresado == "JR":
                if postulante_edad_menor > edad_ingresado:
                    postulante_edad_menor = edad_ingresado
                    postulante_nombre_menor_jr = nombre_ingresado

            match genero_ingresado:
                case "M":
                    suma_edad_m += edad_ingresado
                    contador_masculino += 1
                case "F":
                    suma_edad_f += edad_ingresado
                    contador_femenino += 1
                case _:
                    suma_edad_nb += edad_ingresado
                    contador_no_binario += 1
                    if (tecnologia_ingresado == "ASP.NET" or "JS") and edad_ingresado > 24 and edad_ingresado < 41 and puesto_ingresado == "SSR":
                        cantidad_no_binario += 1

            match tecnologia_ingresado:
                case "PYTHON":
                    contador_python += 1
                case "JS":
                    contador_js += 1
                case _:
                    contador_net += 1        

        if contador_python > contador_js and contador_python > contador_net:
            mas_postulantes_tecnologia = f"PYTHON con {contador_python}"
        elif contador_js > contador_net:
            mas_postulantes_tecnologia = f"JS con {contador_js}"
        else:
            mas_postulantes_tecnologia = f"ASP.NET con {contador_net}"

        contador_total_generos = contador_masculino + contador_femenino + contador_no_binario

        porcentaje_masculino = (contador_masculino * 100) / contador_total_generos
        porcentaje_femenino = (contador_femenino * 100) / contador_total_generos
        porcentaje_no_binario = (contador_no_binario * 100) / contador_total_generos

        promedio_edad_m = suma_edad_m / contador_masculino
        promedio_edad_f = suma_edad_f / contador_femenino
        promedio_edad_nb = suma_edad_nb / contador_no_binario

        print(f"Cantidad de postulantes de genero no binario que sea SSR sepa ASP.NET o JS este entre 25 a 40 años inclusive: {cantidad_no_binario}\nNombre del postulante Jr con menor edad: {postulante_nombre_menor_jr}\nPromedio de edad por genero =\n  Masculino: {promedio_edad_m}\n  Femenino: {promedio_edad_f}\n  No binario: {promedio_edad_nb}\nLa tencnologia mas postulantes {mas_postulantes_tecnologia} \nPorcentaje de postulantes por genero =\n  Masculino: {porcentaje_masculino}\n  Femenino: {porcentaje_femenino}\n  No binario: {porcentaje_no_binario}\n  ")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
