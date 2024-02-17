from abc import ABC, abstractmethod
#factory method

class TareaFactory(ABC):
    @abstractmethod
    def crear_tarea(self):
        pass

class CrearTareaFactory(TareaFactory):
    def crear_tarea(self, nombre="Tarea sin nombre"):
        return CrearTarea(nombre)

class CrearTarea:
    def __init__(self, nombre):
        self.nombre = nombre

    def ejecutar(self):
        
        print(f" Se ha creado la tarea llamada '{self.nombre}'.")


if __name__ == "__main__":
  
    factory = CrearTareaFactory()
    tarea_personalizada = factory.crear_tarea(nombre="Tarea inportante")
    tarea_personalizada.ejecutar()

    
    tarea_predeterminada = factory.crear_tarea()
    tarea_predeterminada.ejecutar()
