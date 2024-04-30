import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Anthony 
apellido:Garay
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_ingresado = prompt("Ingrese un valor", "Numero:")
        numero_ingresado = int(numero_ingresado)

        for numero_actual in range(2,numero_ingresado + 1):
            if numero_actual == 2:
                alert("¿Es primo?",f"El numero {numero_actual} es primo")
                continue
            else:
                for divisor in range(2,numero_actual + 1):
                    if numero_actual % divisor == 0:
                        break

            if divisor == numero_actual:
                alert("¿Es primo?",f"El numero {numero_actual} es primo")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()