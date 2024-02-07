import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Show", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=130,padx=75, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        name = self.txt_nombre().get()
        user = prompt(title = "Enter your username", prompt="Enter your username")
        alert(title = "Personal information",message = f"Your user: {user}")
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()