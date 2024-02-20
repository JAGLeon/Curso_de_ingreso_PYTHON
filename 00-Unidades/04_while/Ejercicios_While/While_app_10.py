import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Anthony
apellido:Garay
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        positivos_ingresados = 0
        negativos_ingresados = 0
        ceros_ingresados = 0
        suma_positivos = 0
        suma_negativos = 0
        numero = 0

        while(numero != None):
            numero = prompt("Numero","Ingrese un valor")
            if numero != None:
                numero = int(numero)
                if numero > 0:
                    suma_positivos += numero
                    positivos_ingresados += 1
                elif numero < 0:
                    suma_negativos += numero
                    negativos_ingresados += 1
                else:
                    ceros_ingresados += 1

        diferencia_positivos_negativos = positivos_ingresados - negativos_ingresados

        if diferencia_positivos_negativos < 0:
            diferencia_positivos_negativos *= -1

        mensaje = f"Suma acumulada de los negativos: {suma_negativos}\nSuma acumulada de los positivos: {suma_positivos}\nPositivos ingresados: {positivos_ingresados}\nNegativos ingresados: {negativos_ingresados}\nCeros ingresados: {ceros_ingresados}\nDiferencia positivos negativos: {diferencia_positivos_negativos}"
        alert("",mensaje)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
