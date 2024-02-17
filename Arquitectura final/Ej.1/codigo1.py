from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk
#twmplate method
class Alimento:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"

class PlantillaPedido(ABC):
    def __init__(self):
        self.articulos = []

    def procesar_pedido(self):
        self.tomar_pedido()
        self.validar_articulos()
        self.preparar_articulos()
        self.calcular_total()

    @abstractmethod
    def tomar_pedido(self):
        pass

    @abstractmethod
    def validar_articulos(self):
        pass

    @abstractmethod
    def preparar_articulos(self):
        pass

    @abstractmethod
    def calcular_total(self):
        pass

class PedidoConMenu(PlantillaPedido):
    MENU = [
        {'nombre': 'Pizza Margherita', 'precio': 40.56},
        {'nombre': 'Pizza Pepperoni', 'precio': 462.99},
        {'nombre': 'Hamburguesa Cheese', 'precio': 567.99},
     
    ]

    def __init__(self):
        super().__init__()

    def mostrar_menu(self, root):
        for i, item in enumerate(self.MENU, start=1):
            tk.Label(root, text=f"{i}. {item['nombre']} - ${item['precio']:.2f}").pack()

    def seleccionar_alimento(self, root):
        seleccion = tk.StringVar()
        seleccion.set("1")  # Por defecto, selecciona la primera opción
        opciones_menu = [f"{i+1}. {item['nombre']} - ${item['precio']:.2f}" for i, item in enumerate(self.MENU)]
        menu_dropdown = ttk.Combobox(root, textvariable=seleccion, values=opciones_menu, state="readonly")
        menu_dropdown.pack()
        return seleccion

    def tomar_pedido(self):
        root = tk.Tk()
        root.title("Selección de Alimentos")

        self.mostrar_menu(root)

        seleccion = self.seleccionar_alimento(root)

        agregar_button = ttk.Button(root, text="Agregar al pedido", command=lambda: self.agregar_alimento(seleccion.get(), root))
        agregar_button.pack()

        finalizar_button = ttk.Button(root, text="Finalizar Pedido", command=root.destroy)
        finalizar_button.pack()

        root.mainloop()

    def agregar_alimento(self, seleccion, root):
        try:
            index = int(seleccion.split('.')[0]) - 1
            alimento = Alimento(self.MENU[index]['nombre'], self.MENU[index]['precio'])
            self.articulos.append(alimento)
            tk.Label(root, text=f"Se ha agregado {alimento.nombre} al pedido.").pack()
        except ValueError:
            tk.Label(root, text="Error al procesar la selección.").pack()

    def validar_articulos(self):
       
        pass

    def preparar_articulos(self):
     
        pass

    def calcular_total(self):
        total = sum(articulo.precio for articulo in self.articulos)
        print(f"Total del pedido: ${total:.2f}")

pedido_menu = PedidoConMenu()
pedido_menu.procesar_pedido()
