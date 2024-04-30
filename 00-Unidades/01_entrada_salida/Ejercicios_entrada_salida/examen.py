import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Anthony
apellido: Garay
dni: 94780539
division: G
---
Ejercicio: entrada_salida_01
---

Enunciado:
De 20 contenedores que llegan al puerto de Rosario, se deben pedir y validar los siguientes datos
Marca (no validar)
Categoría (peligroso, comestible, indumentaria)
Peso ( entre 100 y 800)
Tipo de material ( aluminio, hierro , madera)
Costo en $ (mayor a 0)
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue tipo de material más usado ( aluminio, hierro , madera)
Informe B- El porcentaje de contenedores de Categoría peligroso
Informe C- La marca y tipo del contenedor más pesado
Informe D- La marca del contenedor de comestible con menor costo
Informe E- El promedio de costo de todos los contenedores de HIerro

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=1, sticky="nsew")

    def btn_mostrar_on_click(self):
        contador_contenedor_peligroso = 0
        contador_contenedor_comestible = 0
        contador_contenedor_indumentaria = 0
        contador_aluminio = 0
        contador_hierro = 0
        contador_madera = 0
        acumulador_costo_hierro = 0
        contenedores = 1
        for contenedores in range(1,21):
            marca = prompt("","Ingresar marca")

            categoria = prompt("","Ingresar categoria peligroso, comestible, indumentaria")
            while categoria != "peligroso" and categoria != "comestible" and categoria != "indumentaria":
                categoria = prompt("","Re-ingresar categoria peligroso, comestible, indumentaria")


            peso = prompt("","Ingresar peso entre 100 y 800")
            peso = int(peso)
            while peso < 100 or peso > 800:
                peso = prompt("","Re-ingresar peso entre 100 y 800")
                peso = int(peso)

            tipo = prompt("","Ingresar tipo aluminio, hierro , madera")
            while tipo != "aluminio" and tipo != "hierro" and tipo != "madera":
                tipo = prompt("","Re-ingresar tipo aluminio, hierro , madera")

            costo = prompt("","Ingresar costo mayor a 0")
            costo = int(costo)
            while costo < 1:
                costo = prompt("","Re-ingresar costo mayor a 0")
                costo = int(costo)

            # Informe A
            match tipo:
                case "aluminio":
                    contador_aluminio  += 1
                case "hierro":
                    contador_hierro += 1
                    acumulador_costo_hierro += costo
                case _:
                    contador_madera += 1
            # Informe B
            match categoria:
                case "peligroso":
                    contador_contenedor_peligroso += 1
                case "comestible":
                    # Informe D
                    if contador_contenedor_comestible == 1:
                        marca_contenedor_comestible = marca
                        costo_contenedor_comestible = costo
                    else:
                        if costo_contenedor_comestible > costo:
                            marca_contenedor_comestible = marca
                            costo_contenedor_comestible = costo

                    contador_contenedor_comestible += 1
                case _:
                    contador_contenedor_indumentaria += 1
            
            # Informe C
            if contenedores == 1:
                peso_contenedor_pesado = peso
                marca_contenedor_pesado = marca
                tipo_contenedor_pesado = tipo
            else:
                if peso_contenedor_pesado < peso:
                    peso_contenedor_pesado = peso
                    marca_contenedor_pesado = marca
                    tipo_contenedor_pesado = tipo   
            
            print(f"\nMarca = {marca}\nCategoria = {categoria}\nPeso = {peso}\nTipo = {tipo}\nCosto = {costo}")
        # Informe A
        if contador_aluminio > contador_hierro and contador_aluminio > contador_madera:
            tipo_material_mas_usado = "Aluminio"
        elif contador_hierro > contador_madera:
            tipo_material_mas_usado = "Hierro"
        else:
            tipo_material_mas_usado = "Madera"    
        # Informe B
        porcentaje_contenedor_peligroso = (contador_contenedor_peligroso * 100) / contenedores

        # Informe E
        promedio_costo_hierro = acumulador_costo_hierro / contador_hierro

        print(f"El tipo de material más usado = {tipo_material_mas_usado}\nEl porcentaje de contenedores de Categoría peligroso = {porcentaje_contenedor_peligroso}\nLa marca y tipo del contenedor más pesado = {marca_contenedor_pesado} {tipo_contenedor_pesado}\nLa marca del contenedor de comestible con menor costo = {marca_contenedor_comestible}\nEl promedio de costo de todos los contenedores de HIerro = {promedio_costo_hierro}")  

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
