import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Anthony
apellido: Garay
---
Ejercicio: entrada_salida_01
---
Enunciado:
para saber el costo de un viaje necesitamos el siguiente algoritmo,
sabiendo que el precio por kilo de pasajero es 1000 pesos
Se ingresan todos los datos por PROMPT
los datos a solicitar de dos personas son,
nombre, edad y peso
se pide  armar el siguiente mensaje
"hola jose y maria , sus pesos son 80 kilos y 60 kilos respectivamente
, sumados da 140 kilos , el promedio de edad es 33 y su viaje vale 140 000 pesos".
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=1, sticky="nsew")

    def btn_mostrar_on_click(self):
        precio_por_kilo = 1000

        primer_persona_nombre = prompt("Datos","Nombre")
        primer_persona_edad = prompt("Datos","Edad")
        primer_persona_peso = prompt("Datos","Peso")
        primer_persona_edad_int = int(primer_persona_edad)
        primer_persona_peso_int = int(primer_persona_peso)


        segunda_persona_nombre = prompt("Datos","Nombre")
        segunda_persona_edad = prompt("Datos","Edad")
        segunda_persona_peso = prompt("Datos","Peso")
        segunda_persona_edad_int = int(segunda_persona_edad)
        segunda_persona_peso_int = int(segunda_persona_peso)

        suma_de_peso = primer_persona_peso_int + segunda_persona_peso_int
        suma_de_edad = segunda_persona_edad_int + primer_persona_edad_int
        promedio_de_edad = suma_de_edad / 2
        
        precio_viaje = suma_de_peso * precio_por_kilo

        mensaje = f"hola {primer_persona_nombre} y {segunda_persona_nombre} , sus pesos son {primer_persona_peso} kilos y {segunda_persona_peso} kilos respectivamente, sumados da {suma_de_peso} kilos , el promedio de edad es {promedio_de_edad} y su viaje vale {precio_viaje} pesos"
        alert("Pasaje", mensaje)
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
