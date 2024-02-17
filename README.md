# DesignPatterns
Nicolas Rodriguez, Santiago Romero, Jhonathan Vergara.

Diagramas de clases:






1 y 2:


https://docs.google.com/document/d/1b3yJee7PALNPTeq51IfMhc-6u4irxG0j/edit?usp=sharing&ouid=114589523439964235465&rtpof=true&sd=true



3 y 4:


https://lucid.app/lucidchart/d54de414-60f7-4a01-81ce-d6dc203d5c3f/edit?viewport_loc=199%2C106%2C1150%2C653%2CHWEp-vi-RSFO&invitationId=inv_8411885e-a2bb-4d87-9968-3d85c83c1404


5:
https://lucid.app/lucidchart/62088897-e262-474d-8f2c-ef1a0508fa48/edit?viewport_loc=-249%2C136%2C1925%2C1093%2CHWEp-vi-RSFO&invitationId=inv_ae2ee10f-0b6b-4290-a562-e06aa541b32a


Descripciones:


1.	En el primer ejercicio , se implementó el patrón Template Method, La clase abstracta PlantillaPedido define un esqueleto con métodos abstractos que son implementados por las clases concretas. Este patrón permite mantener la consistencia en el proceso de pedido mientras permite modificaciones.

2.El segundo punto utiliza el patrón Factory Method ,  TareaFactory define el método crear_tarea, delegando la responsabilidad de la creación a las subclases como CrearTareaFactory. Este patrón facilita la extensión del sistema con nuevas implementaciones de tareas sin modificar el código existente.

3.En el tercer ejercicio, se implementa el patrón Builder ,   MenuConstructor actúa como el director que supervisa la construcción, mientras que las clases DirectorRestaurante y InterfazMenu representan el proceso de construcción.


4.El cuarto ejercicio  emplea el patrón Decorator , La clase base Habitacion establece la estructura básica, mientras que las clases decoradoras como DecoradorFlores y DecoradorChocolate añaden funcionalidades adicionales.



5.En el quinto ejercicio  se implementa el patrón Abstract Factory  EnvioFactory y ServicioFactory definen métodos para crear instancias de envío y servicio, respectivamente. Las clases concretas, como EnvioTerrestreFactory y ServicioEstandarFactory, implementan estas interfaces, permitiendo la creación de familias de objetos relacionados sin especificar sus clases concretas
