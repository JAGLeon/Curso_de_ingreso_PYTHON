import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Anthony 
apellido:Garay
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        ingresar = "s"
        bandera_cantidad_candidatos = 0
        suma_edades = 0
        suma_votos_emitidos = 0

        while ingresar == "s":
            candidato_nombre = prompt("Ingrese","Nombre")

            candidato_edad = prompt("Ingrese","Edad")
            candidato_edad = int(candidato_edad)
            while candidato_edad < 25:
                candidato_edad = prompt("Re-ingrese","Edad")
                candidato_edad = int(candidato_edad)

            candidato_cantidad_votos = prompt("Ingrese","Votos")
            candidato_cantidad_votos = int(candidato_cantidad_votos)
            while candidato_cantidad_votos < 0:     
                candidato_cantidad_votos = prompt("Re-ingrese","Votos")
                candidato_cantidad_votos = int(candidato_cantidad_votos)


            if bandera_cantidad_candidatos == 0:
                nombre_candidato_mas_votado = candidato_nombre
                votos_candidato_mas_votado = candidato_cantidad_votos

                nombre_candidato_menos_votos = candidato_nombre
                votos_candidato_menos_votado = candidato_cantidad_votos
                edad_candidato_menos_votado = candidato_edad
            else:
                if votos_candidato_mas_votado < candidato_cantidad_votos:
                    nombre_candidato_mas_votado = candidato_nombre
                elif votos_candidato_menos_votado > candidato_cantidad_votos:
                    nombre_candidato_menos_votos = candidato_nombre
                    edad_candidato_menos_votado = candidato_edad

            suma_edades += candidato_edad
            suma_votos_emitidos += candidato_cantidad_votos
            bandera_cantidad_candidatos += 1

            ingresar = prompt("Desea cargar otro cantidato","Ingrese la letra s para seguir")

        promedio_edades = suma_edades / bandera_cantidad_candidatos

        alert("Paso del mes de Octubre",f"Candidato más votado {nombre_candidato_mas_votado}\nCandidato {nombre_candidato_menos_votos} menos votado de {edad_candidato_menos_votado} años\nPromedio edades candidatos {promedio_edades}\nTotal votos emitidos {suma_votos_emitidos}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
