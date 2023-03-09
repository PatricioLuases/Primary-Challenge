from enum import Enum

class Tipo(Enum):
    URBANA=1
    DEPORTIVA=2

class Vehiculo:
    def __init__(self,color,ruedas) -> None:
        self.color=color
        self.ruedas=ruedas

class Coche(Vehiculo):
    def __init__(self, color, ruedas,velocidad,cilindrada) -> None:
        super().__init__(color, ruedas) 
        self.velocidad=velocidad
        self.cilindrada=cilindrada

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas,tipo) -> None:
        super().__init__(color, ruedas)
        self.tipo=tipo

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada,carga) -> None:
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga=carga

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo,velocidad,cilindrada) -> None:
        super().__init__(color, ruedas, tipo)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
