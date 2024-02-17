import tkinter as tk
from tkinter import ttk
#builder
class Menu:
    def __init__(self):
        self.plato_principal = None
        self.entrante = None
        self.postre = None

    def __str__(self):
        return f"Menú: {self.plato_principal}, {self.entrante}, {self.postre}"

class MenuConstructor:
    def __init__(self):
        self.menu = Menu()

    def set_plato_principal(self, plato):
        self.menu.plato_principal = plato

    def set_entrante(self, entrante):
        self.menu.entrante = entrante

    def set_postre(self, postre):
        self.menu.postre = postre

    def obtener_menu(self):
        return self.menu

class DirectorRestaurante:
    def __init__(self, constructor_menu):
        self.constructor_menu = constructor_menu

    def construir_menu_vegetariano(self):
        self.constructor_menu.set_plato_principal("Hamburguesa de lentejas")
        self.constructor_menu.set_entrante("Ensalada de quinoa")
        self.constructor_menu.set_postre("Tarta de frutas")

    def construir_menu_infantil(self):
        self.constructor_menu.set_plato_principal("Nuggets de pollo")
        self.constructor_menu.set_entrante("Palitos de zanahoria")
        self.constructor_menu.set_postre("Helado")

class InterfazMenu:
    def __init__(self, constructor_menu):
        self.constructor_menu = constructor_menu
        self.root = tk.Tk()
        self.root.title("Constructor de Menú")

        self.label = tk.Label(self.root, text="Seleccione los platos para el menú:")
        self.label.pack(pady=10)

        self.plato_principal_var = tk.StringVar()
        self.entrante_var = tk.StringVar()
        self.postre_var = tk.StringVar()

        self.create_dropdown("Plato Principal", self.plato_principal_var)
        self.create_dropdown("Entrante", self.entrante_var)
        self.create_dropdown("Postre", self.postre_var)

        self.build_button = tk.Button(self.root, text="Construir Menú", command=self.construir_menu)
        self.build_button.pack(pady=20)

    def create_dropdown(self, label_text, variable):
        label = tk.Label(self.root, text=label_text)
        label.pack()

        options = ["", "Hamburguesa de lentejas", "Ensalada de quinoa", "Tarta de frutas",
                   "Nuggets de pollo", "Palitos de zanahoria", "Helado"]

        dropdown = ttk.Combobox(self.root, textvariable=variable, values=options, state="readonly")
        dropdown.pack(pady=10)

    def construir_menu(self):
        self.constructor_menu.set_plato_principal(self.plato_principal_var.get())
        self.constructor_menu.set_entrante(self.entrante_var.get())
        self.constructor_menu.set_postre(self.postre_var.get())

        menu = self.constructor_menu.obtener_menu()
        print(f"Menú construido: {menu}")

    def run(self):
        self.root.mainloop()


constructor_menu = MenuConstructor()
director_restaurante = DirectorRestaurante(constructor_menu)
interfaz_menu = InterfazMenu(constructor_menu)


director_restaurante.construir_menu_vegetariano()


interfaz_menu.run()
