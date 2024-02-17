import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod
#abstract factory

def calcular_costo_envio(tipo_envio):
    if tipo_envio == "terrestre":
        costo = 100
    elif tipo_envio == "maritimo":
        costo = 200
    elif tipo_envio == "aereo":
        costo = 300
    else:
        raise ValueError(f"Tipo de envío desconocido: {tipo_envio}")

    return costo


def estimar_tiempo_entrega(tipo_envio):
    if tipo_envio == "terrestre":
        tiempo_entrega = 3
    elif tipo_envio == "maritimo":
        tiempo_entrega = 10
    elif tipo_envio == "aereo":
        tiempo_entrega = 1
    else:
        raise ValueError(f"Tipo de envío desconocido: {tipo_envio}")

    return tiempo_entrega


class Envio(ABC):
    @abstractmethod
    def realizar_seguimiento(self):
        pass

    @abstractmethod
    def contratar_seguro(self):
        pass

class EnvioTerrestre(Envio):
    def realizar_seguimiento(self):
        print("Realizando seguimiento de envío terrestre...")

    def contratar_seguro(self):
        print("Contratando seguro para envío terrestre...")

class EnvioMaritimo(Envio):
    def realizar_seguimiento(self):
        print("Realizando seguimiento de envío marítimo...")

    def contratar_seguro(self):
        print("Contratando seguro para envío marítimo...")

class EnvioAereo(Envio):
    def realizar_seguimiento(self):
        print("Realizando seguimiento de envío aéreo...")

    def contratar_seguro(self):
        print("Contratando seguro para envío aéreo...")

class Servicio(ABC):
    @abstractmethod
    def realizar_seguimiento(self):
        pass

    @abstractmethod
    def contratar_seguro(self):
        pass

class ServicioEstandar(Servicio):
    def realizar_seguimiento(self):
        print("Realizando seguimiento de servicio estándar...")

    def contratar_seguro(self):
        print("Contratando seguro para servicio estándar...")

class ServicioExpress(Servicio):
    def realizar_seguimiento(self):
        print("Realizando seguimiento de servicio express...")

    def contratar_seguro(self):
        print("Contratando seguro para servicio express...")


class EnvioFactory(ABC):
    @abstractmethod
    def crear_envio(self):
        pass

class EnvioTerrestreFactory(EnvioFactory):
    def crear_envio(self):
        return EnvioTerrestre()

class EnvioMaritimoFactory(EnvioFactory):
    def crear_envio(self):
        return EnvioMaritimo()

class EnvioAereoFactory(EnvioFactory):
    def crear_envio(self):
        return EnvioAereo()

class ServicioFactory(ABC):
    @abstractmethod
    def crear_servicio(self):
        pass

class ServicioEstandarFactory(ServicioFactory):
    def crear_servicio(self):
        return ServicioEstandar()

class ServicioExpressFactory(ServicioFactory):
    def crear_servicio(self):
        return ServicioExpress()

class AplicacionEnvio(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Envíos")
        self.geometry("400x200")

        self.label_tipo_envio = tk.Label(self, text="Tipo de Envío:")
        self.combo_tipo_envio = ttk.Combobox(self, values=["terrestre", "maritimo", "aereo"])

        self.label_tipo_servicio = tk.Label(self, text="Tipo de Servicio:")
        self.combo_tipo_servicio = ttk.Combobox(self, values=["estandar", "express"])

       
        self.btn_procesar = tk.Button(self, text="Procesar Envío", command=self.procesar_envio)

        
        self.resultado_text = tk.Text(self, height=5, width=40, state="disabled")

        self.label_tipo_envio.grid(row=0, column=0, padx=10, pady=5)
        self.combo_tipo_envio.grid(row=0, column=1, padx=10, pady=5)
        self.label_tipo_servicio.grid(row=1, column=0, padx=10, pady=5)
        self.combo_tipo_servicio.grid(row=1, column=1, padx=10, pady=5)
        self.btn_procesar.grid(row=2, column=0, columnspan=2, pady=10)
        self.resultado_text.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def procesar_envio(self):
        tipo_envio = self.combo_tipo_envio.get()
        tipo_servicio = self.combo_tipo_servicio.get()

        fabrica_envio = None
        fabrica_servicio = None

        if tipo_envio == "terrestre":
            fabrica_envio = EnvioTerrestreFactory()
        elif tipo_envio == "maritimo":
            fabrica_envio = EnvioMaritimoFactory()
        elif tipo_envio == "aereo":
            fabrica_envio = EnvioAereoFactory()
        else:
            self.mostrar_resultado(f"Tipo de envío desconocido: {tipo_envio}")
            return

        envio = fabrica_envio.crear_envio()

        if tipo_servicio == "estandar":
            fabrica_servicio = ServicioEstandarFactory()
        elif tipo_servicio == "express":
            fabrica_servicio = ServicioExpressFactory()
        else:
            self.mostrar_resultado(f"Tipo de servicio desconocido: {tipo_servicio}")
            return

        servicio = fabrica_servicio.crear_servicio()

        costo = calcular_costo_envio(tipo_envio)
        tiempo_entrega = estimar_tiempo_entrega(tipo_envio)

        resultado = f"Tipo de envío: {tipo_envio}\nCosto: {costo}\nTiempo de entrega: {tiempo_entrega}\nServicio: {tipo_servicio}"
        self.mostrar_resultado(resultado)

    def mostrar_resultado(self, resultado):
        self.resultado_text.config(state="normal")
        self.resultado_text.delete("1.0", tk.END)
        self.resultado_text.insert(tk.END, resultado)
        self.resultado_text.config(state="disabled")


if __name__ == "__main__":
    app = AplicacionEnvio()
    app.mainloop()
