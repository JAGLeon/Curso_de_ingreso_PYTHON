
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


"""

nombre: Anthony
apellido: Garay
En el parque de diversiones "Aventuras Extremas", un grupo de 10 amigos ha
decidido disfrutar del día probando las diferentes atracciones y luego se reúnen en un
restaurante para compartir un delicioso almuerzo. Antes de que llegue la cuenta, deciden
crear un programa para calcular y dividir los gastos de manera equitativa.
Se pide ingresar los siguientes datos hasta que el usuario lo desee:

Para cada amigo (pedir por prompt)

Nombre del amigo, #NO NO NO NO SE VALIDA (NO HACE FALTA)
Plato principal elegido ("Pizza", "Hamburguesa", "Ensalada").
Cantidad de platos principales pedidos (debe ser al menos 2).

Bebida elegida ("Refresco", "Agua", "Jugo").
Cantidad de bebidas pedidas (debe ser al menos 2).


Se conocen los siguientes precios base:

El precio unitario de cada plato principal es de $3000.

El precio unitario de cada bebida es de $1000.


Una vez ingresados todos los datos, el programa debe calcular e informar lo siguiente (informar por print):

Informar cual fue el tipo de bebida más vendida.
Los porcentajes de cada tipo de platos pedidos (teniendo en cuenta su cantidad). Ejemplo: [30% pizza, 40% ensaladas,
30% hamburguesas]
Informar la cantidad total de bebidas que fueron “Refresco”.
El promedio gastado en platos principales de tipo “Pizza” sobre el grupo de amigos en general.
El nombre de la persona que pidió la menor cantidad de platos principales de tipo “Hamburguesa”

bis
cantidad de usuarios que pidieron mas de una bebida
cantidad de amigos que pidieron menos de un plato principal

el nombre del que compro mas bebidas
el nombre del que menos platos principales pidio

el nombre de la persona que pidio mas pizzas
el promedio de bebidas por persona
el precio promedio de bebidas pagada por cada persona
"""

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=1, sticky="nsew")

    def btn_mostrar_on_click(self):
        continuar = True
        precio_unitario_plato_principal= 3000
        precio_unitario_bebida = 1000
        acumulador_cantidad_refresco = 0
        acumulador_cantidad_agua = 0
        acumulador_cantidad_jugo = 0
        acumulador_cantidad_pizza = 0
        acumulador_cantidad_hamburguesa = 0
        acumulador_cantidad_ensalada = 0
        acumulador_cantidad_refresco = 0
        contador_personas_pidieron_pizza = 0
        contador_hamburguesa = 0
        contador_mas_dos_bebidas = 0
        contador_dos_platos = 0
        amigos_ingresados = 0
        while continuar:
            nombre_ingresado = prompt("","Ingresar nombre")

            plato_ingresado = prompt("","Ingresar plato")
            while plato_ingresado != "pizza" and plato_ingresado != "hamburguesa" and plato_ingresado != "ensalada":
                plato_ingresado = prompt("ERROR","Re-ingresar plato")

            plato_cantidad_ingresado = prompt("","Ingresar cantidad platos")
            plato_cantidad_ingresado = int(plato_cantidad_ingresado)
            while plato_cantidad_ingresado < 2:
                plato_cantidad_ingresado = prompt("ERROR","Re-ingresar cantidad platos, 2 por lo menos")
                plato_cantidad_ingresado = int(plato_cantidad_ingresado)

            bebida_ingresado = prompt("","Ingresar bebida")
            while bebida_ingresado != "refresco" and bebida_ingresado != "agua" and bebida_ingresado != "jugo":
                bebida_ingresado = prompt("ERROR","Re-ingresar bebida")

            bebida_cantidad_ingresado = prompt("","Ingresar cantidad bebidas")
            bebida_cantidad_ingresado = int(bebida_cantidad_ingresado)
            while bebida_cantidad_ingresado < 2:
                bebida_cantidad_ingresado = prompt("ERROR","Re-ingresar cantidad bebidas, 2 por lo menos")
                bebida_cantidad_ingresado = int(bebida_cantidad_ingresado)

            match bebida_ingresado:
                case "refresco":
                    acumulador_cantidad_refresco += bebida_cantidad_ingresado
                case "agua":
                    acumulador_cantidad_agua += bebida_cantidad_ingresado
                case _:
                    acumulador_cantidad_jugo += bebida_cantidad_ingresado

            if bebida_cantidad_ingresado > 2:
                contador_mas_dos_bebidas += 1

            if plato_cantidad_ingresado == 2:
                contador_dos_platos += 1

            if amigos_ingresados == 0:
                nombre_compro_mas_bebidas = nombre_ingresado
                cantidad_mas_bebidas = bebida_cantidad_ingresado
                nombre_compro_menos_platos = nombre_ingresado
                cantidad_menos_platos = plato_cantidad_ingresado
            else:
                if cantidad_mas_bebidas < bebida_cantidad_ingresado:
                    nombre_compro_mas_bebidas = nombre_ingresado
                    cantidad_mas_bebidas = bebida_cantidad_ingresado

                if cantidad_menos_platos > plato_cantidad_ingresado:
                    nombre_compro_menos_platos = nombre_ingresado
                    cantidad_menos_platos = plato_cantidad_ingresado

            match plato_ingresado:
                case "pizza":
                    if contador_personas_pidieron_pizza == 0:
                        nombre_mas_cantidad_pizza = nombre_ingresado
                        mas_cantidad_pizza = plato_cantidad_ingresado
                    else:
                        if mas_cantidad_pizza < plato_cantidad_ingresado:
                            nombre_mas_cantidad_pizza = nombre_ingresado
                            mas_cantidad_pizza = plato_cantidad_ingresado

                    contador_personas_pidieron_pizza += 1
                    acumulador_cantidad_pizza += plato_cantidad_ingresado
                case "hamburguesa":
                    if contador_hamburguesa == 0:
                        nombre_menor_cantidad_hamburguesa = nombre_ingresado
                        menor_cantidad_hamburguesa = plato_cantidad_ingresado
                    else:
                        if menor_cantidad_hamburguesa > plato_cantidad_ingresado:
                            nombre_menor_cantidad_hamburguesa = nombre_ingresado
                            menor_cantidad_hamburguesa = plato_cantidad_ingresado

                    acumulador_cantidad_hamburguesa += plato_cantidad_ingresado
                    contador_hamburguesa += 1
                case _:
                    acumulador_cantidad_ensalada += plato_cantidad_ingresado

            amigos_ingresados += 1

            print(f"\nNombre = {nombre_ingresado}\nPlato = {plato_ingresado} unidades {plato_cantidad_ingresado}\nBebida = {bebida_ingresado} unidades {bebida_cantidad_ingresado}\n")

            continuar = question("", "Desea seguir ingresando datos, click 'SI'")

        suma_bebidas = acumulador_cantidad_refresco + acumulador_cantidad_agua + acumulador_cantidad_jugo
        #promedio_precio_bebidas = (suma_bebidas * precio_unitario_bebida) / amigos_ingresados
        promedio_bebidas_persona = suma_bebidas / amigos_ingresados
        promedio_precio_bebidas = promedio_bebidas_persona * precio_unitario_bebida

        if acumulador_cantidad_refresco > acumulador_cantidad_agua and acumulador_cantidad_refresco > acumulador_cantidad_jugo:
            mensaje_bebida = f"Refresco"
        elif acumulador_cantidad_agua > acumulador_cantidad_jugo:
            mensaje_bebida = f"Agua"
        else:
            mensaje_bebida = f"Jugo"

        promedio_gastado_pizza = (acumulador_cantidad_pizza * precio_unitario_plato_principal) / contador_personas_pidieron_pizza

        suma_total_plato = acumulador_cantidad_pizza + acumulador_cantidad_hamburguesa + acumulador_cantidad_ensalada
        porcentaje_pizza = (acumulador_cantidad_pizza * 100) / suma_total_plato
        porcentaje_hamburguesa = (acumulador_cantidad_hamburguesa * 100) / suma_total_plato
        porcentaje_ensalada = (acumulador_cantidad_ensalada * 100) / suma_total_plato

        print(f"Bebida más vendida = {mensaje_bebida}\nPromedios pizza = {porcentaje_pizza}%\nPromedios hamburguesa = {porcentaje_hamburguesa}%\nPromedios ensalada = {porcentaje_ensalada}%\nTotal bebidas {acumulador_cantidad_refresco} Refresco\nPromedio gastado en pizza = {promedio_gastado_pizza}\nNombre de la persona que pidio menos hamburguesas = {nombre_menor_cantidad_hamburguesa}\nBIS\nCantidad de usuarios que pidieron mas de 2 bebidas {contador_mas_dos_bebidas}\nCantidad de amigos que pidieron 2 platos {contador_dos_platos}\nNombre compro mas bebidas = {nombre_compro_mas_bebidas}\nNombre del que menos platos pidio = {nombre_compro_menos_platos}\nNombre persona que pidio mas pizza = {nombre_mas_cantidad_pizza}\nPromedio bebidas por persona = {promedio_bebidas_persona}\nPromedio precio de bebidas a pagar por persona = {promedio_precio_bebidas}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()