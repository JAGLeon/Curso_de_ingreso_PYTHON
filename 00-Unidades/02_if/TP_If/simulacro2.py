import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Anthony
apellido: Garay
---
Ejercicio: simulacro2
---
La empresa spaceX , nos contrata para poder hacer el cálculo de precio final y descuentos para un viaje al espacio exterior
el costo por millón de kilómetros es de 8 bitcoin 

podes viajar a Marte (60 millones de KM) , la Luna (½ millón de KM)y a Titan (1300 millones de KM)
podes elegir si viajar en verano, primavera  otoño o invierno.

para los viajes a Marte
Si viajan más de 5 personas te hacemos un 50 % de descuento sobre el precio,
viajando en verano al precio con descuento se le suma un 10% , en otoño y primavera se le suma un 25% al precio con descuento.

para los viajes la Luna 
si viajan más de 5 personas te hacemos un 40 % de descuento sobre el precio,
viajando en verano al precio con descuento se le suma un 15% ,  en otoño y primavera al precio con descuento se le suma un 25%

para los viajes a Titan
si viajan más de 5 personas te hacemos un 30 % de descuento sobre el precio,
viajando en verano al precio final se le suma un 10% , en otoño y primavera al precio con descuento se le suma un 20%

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=1, sticky="nsew")


    def btn_mostrar_on_click(self):
        un_kilometro = 8
        descuento = 0
        aumento_temporada = 0

        destino = prompt(title = "Destino", prompt="Ingresa tu destino")
        temporada = prompt(title = "Temporada", prompt="Ingresa la temporada")
        personas = prompt(title = "Personas", prompt="Ingresa tu personas")
        personas = int(personas)

        match destino:
            case "Marte":
                precio_destino = 60000000

                if personas > 5:
                    descuento = 50

                match temporada:
                    case "Verano":
                        aumento_temporada = 10
                    case "Otoño" | "Primavera":
                        aumento_temporada = 25

            case "Luna":
                precio_destino = 500000

                if personas > 5:
                    descuento = 40

                match temporada:
                    case "Verano":
                        aumento_temporada = 15
                    case "Otoño" | "Primavera":
                        aumento_temporada = 25

            case "Titan":
                precio_destino = 1300000000

                if personas > 5:
                    descuento = 30

                match temporada:
                    case "Verano":
                        aumento_temporada = 10
                    case "Otoño" | "Primavera":
                        aumento_temporada = 20
            case _:
                precio_destino = 0

        if precio_destino > 0:
            precio_bruto = un_kilometro * precio_destino
            precio_descuento = precio_bruto * descuento / 100
            precio_neto = precio_bruto - precio_descuento
            mensaje = f"Precio destino = {precio_destino}\nPersonas = {personas}\nPrecio bruto = {precio_bruto}\nPrecio descuento = {precio_descuento}\nValor de viaje a marte = {precio_neto} btc"

            if aumento_temporada > 0:
                precio_aumento_temporada = precio_neto * aumento_temporada / 100
                precio_neto_temporada = precio_neto + precio_aumento_temporada
                mensaje = f"Precio destino = {precio_destino}\nPersonas = {personas}\nPrecio bruto = {precio_bruto}\nPrecio descuento = {precio_descuento}\nPrecio aumento por temporada = {precio_aumento_temporada}\nValor de viaje a marte = {precio_neto_temporada} btc"
        else:
            mensaje = "Aun no llegamos a esa parte del mundo"

        # precio_destino = '{:,}'.format(precio_destino) 
        # mensaje = precio_destino
        alert(f"{destino} {temporada}",mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()