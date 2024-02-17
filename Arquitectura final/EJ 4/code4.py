import tkinter as tk
from tkinter import ttk
#decorator
class Habitacion:
    def __init__(self):
        self.descripcion = "Habitación Básica"
        self.costo = 100.0
        self.mejoras = []

    def obtener_descripcion(self):
        return self.descripcion

    def obtener_costo(self):
        return self.costo

    def obtener_mejoras_aplicadas(self):
        return self.mejoras

# Decorador Abstracto
class Decorador(object):
    def __init__(self, habitacion):
        self.habitacion = habitacion

    def obtener_descripcion(self):
        return self.habitacion.obtener_descripcion()

    def obtener_costo(self):
        return self.habitacion.obtener_costo()

    def obtener_mejoras_aplicadas(self):
        return self.habitacion.obtener_mejoras_aplicadas()


class DecoradorFlores(Decorador):
    def __init__(self, habitacion):
        super().__init__(habitacion)
        self.descripcion = ", con Flores Frescas"
        self.costo = 20.0

    def obtener_mejoras_aplicadas(self):
        mejoras = self.habitacion.obtener_mejoras_aplicadas()
        mejoras.append("Flores Frescas")
        return mejoras

class DecoradorChocolate(Decorador):
    def __init__(self, habitacion):
        super().__init__(habitacion)
        self.descripcion = ", con Chocolate Gourmet"
        self.costo = 15.0

    def obtener_mejoras_aplicadas(self):
        mejoras = self.habitacion.obtener_mejoras_aplicadas()
        mejoras.append("Chocolate Gourmet")
        return mejoras

class DecoradorVino(Decorador):
    def __init__(self, habitacion):
        super().__init__(habitacion)
        self.descripcion = ", con Vino de Alta Calidad"
        self.costo = 25.0

    def obtener_mejoras_aplicadas(self):
        mejoras = self.habitacion.obtener_mejoras_aplicadas()
        mejoras.append("Vino de Alta Calidad")
        return mejoras


def decorar_habitacion(habitacion, mejoras):
    for mejora in mejoras:
        if mejora == "Flores":
            habitacion = DecoradorFlores(habitacion)
        elif mejora == "Chocolate":
            habitacion = DecoradorChocolate(habitacion)
        elif mejora == "Vino":
            habitacion = DecoradorVino(habitacion)
    return habitacion

class InterfazHabitacion:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Decorador de Habitación")

        self.habitacion = Habitacion()

        self.label = tk.Label(self.root, text="Seleccione mejoras para la habitación:")
        self.label.pack(pady=10)

        self.mejoras_var = tk.StringVar()
        self.mejoras_var.set("Flores")  

        self.mejoras_dropdown = ttk.Combobox(self.root, textvariable=self.mejoras_var, values=["Flores", "Chocolate", "Vino"], state="readonly")
        self.mejoras_dropdown.pack(pady=10)

        self.decorar_button = tk.Button(self.root, text="Decorar Habitación", command=self.decorar_habitacion)
        self.decorar_button.pack(pady=20)

    def decorar_habitacion(self):
        mejoras_seleccionadas = self.mejoras_var.get().split(", ")
        habitacion_decorada = decorar_habitacion(self.habitacion, mejoras_seleccionadas)

        resultado_label = tk.Label(self.root, text=f"Descripción: {habitacion_decorada.obtener_descripcion()}\n"
                                                    f"Costo: ${habitacion_decorada.obtener_costo():.2f}\n"
                                                    f"Mejoras Aplicadas: {', '.join(habitacion_decorada.obtener_mejoras_aplicadas())}")
        resultado_label.pack(pady=20)

    def run(self):
        self.root.mainloop()

interfaz_habitacion = InterfazHabitacion()
interfaz_habitacion.run()
