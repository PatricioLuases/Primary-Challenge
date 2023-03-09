from ClassDefinitions import Vehiculo
from ClassDefinitions import Coche
from ClassDefinitions import Bicicleta
from ClassDefinitions import Camioneta
from ClassDefinitions import Motocicleta
from ClassDefinitions import Tipo


'''
Ejercicio 1:
Crea al menos un objeto de cada subclase y añadelos a una lista llamada
vehículos.

'''

def crearListaVehiculos():
    coche=Coche("Rojo", 4, 120,300)
    bicicleta=Bicicleta("Verde",2,Tipo.DEPORTIVA)
    camioneta=Camioneta("Gris",4,100,150,1000)
    motocicleta=Motocicleta("Azul",2,Tipo.URBANA,100,125)

    vehiculos=list()
    vehiculos.append(coche)
    vehiculos.append(bicicleta)
    vehiculos.append(camioneta)
    vehiculos.append(motocicleta)
    return vehiculos

'''
Ejercicio 2
Realiza una función llamada catalogar() que reciba la lista de vehículos y los
recorra mostrando el nombre de su clase y sus atributos.
'''

def catalogar(vehiculos):
    for vehiculo in vehiculos:
            print("Nombre de la clase: " + vehiculo.__class__.__name__)
            print("Los atributos de la clase son: " + ", ".join(vehiculo.__dict__.keys()))
            print("---------")


'''
Ejercicio 3:
Modifica la función catalogar() para que reciba un argumento optativo ruedas,
haciendo que muestre únicamente los que su número de ruedas concuerde con
el valor del argumento. También debe mostrar un mensaje "Se han encontrado
{} vehículos con {} ruedas:" únicamente si se envía el argumento ruedas. Ponla a
prueba con 0, 2 y 4 ruedas como valor.
'''

def catalogarEj3(vehiculos,ruedas=None):
    cantidad=0
    for vehiculo in vehiculos:
            if ruedas is None or vehiculo.ruedas == ruedas:
                print("Nombre de la clase: " + vehiculo.__class__.__name__)
                print("Atributos de la clase: " + ", ".join(vehiculo.__dict__.keys()))
                print("---------")
                if ruedas is not None:
                    cantidad+=1
    if ruedas is not None:
         print("Se han encontrado " + str(cantidad) + " vehículos con " + str(ruedas) + " ruedas.",end="\n\n")



def main():
    vehiculos=crearListaVehiculos()
    print("Main: Invocando a la funcion catalogar sin modificar:",end="\n\n")
    catalogar(vehiculos)
    print("Main: Invocando a la funcion catalogar modificada con ruedas=0:",end="\n\n")
    catalogarEj3(vehiculos,0)
    print("Main: Invocando a la funcion catalogar modificada con ruedas=2:",end="\n\n")
    catalogarEj3(vehiculos,2)
    print("Main: Invocando a la funcion catalogar modificada con ruedas=4:",end="\n\n")
    catalogarEj3(vehiculos,4)

if __name__ == "__main__":
    main()
