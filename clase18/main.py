# traductorDeBaseDeDatos = {
#     "0": "clase",
#     "1": "color",
#     "2": "ruedas",
#     "3": "velocidad",
#     "4": "cilindrada",
#     "5": "tipo",
#     "6": "carga"
# }

traductorDeBaseDeDatos = {
    "clase": 0,
    "color": 1,
    "ruedas": 2,
    "velocidad": 3,
    "cilindrada": 4,
    "tipo": 5,
    "carga": 6
}


class Vehiculo():

    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def catalogar(self):
        print("Este es un vehiculo con {} ruedas y de tal {} color".format(self.ruedas,self.color))

    def toString(self):
        return "Vehiculo," + self.color + "," + str(self.ruedas) + "," + 'X,X,X,X'

class Coche(Vehiculo):

    def __init__(self,color,ruedas,velocidad,cilindrada):
        Vehiculo.__init__(self,color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def catalogar(self):
        print("Este es un coche con {} ruedas, de tal {} color, con una velocidad de {} y {} cilindrada".format(self.ruedas,self.color,self.velocidad,self.cilindrada))

    def toString(self):
        return "Coche," + self.color + "," + str(self.ruedas) + "," + str(self.velocidad) + "," + str(self.cilindrada) + "," + 'X,X'

class Bicicleta(Vehiculo):
        
    def __init__(self,color,ruedas,tipo):
        Vehiculo.__init__(self,color,ruedas)
        self.tipo = tipo

    def catalogar(self):
        print("Este es una bicicleta con {} ruedas, de color {} y de tipo {}".format(self.ruedas,self.color,self.tipo))

    def toString(self):
        return "Bicicleta," + self.color + "," + str(self.ruedas) + "," + "X,X," + str(self.tipo) + "," +'X'

class Camioneta(Coche):

    def __init__(self,color,ruedas,velocidad,cilindrada,carga):
        Coche.__init__(self,color,ruedas,velocidad,cilindrada)
        self.carga = carga

    def catalogar(self):
        print("Este es un camioneta con {} ruedas, de color {} , con una velocidad de {}, {} cilindrada y con una capacidad de carga de {} kg".format(self.ruedas,self.color,self.velocidad,self.cilindrada,self.carga))

class Motocicleta(Bicicleta):

    def __init__(self,color,ruedas,tipo,velocidad,cilindrada):
        Bicicleta.__init__(self,color,ruedas,tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def catalogar(self):
        print("Este es una motocicleta con {} ruedas, de  color {} , con una velocidad de {}, {} cilindrada y de tipo {}".format(self.ruedas,self.color,self.velocidad,self.cilindrada,self.tipo))


def escribirBaseDeDatos(listaDeVehiculos):
    archivo = open("baseDeDatos.txt", "w")
    print("Escritura Iniciada")
    for vehiculo in listaDeVehiculos:
        archivo.write( vehiculo.toString() +'\n')
    archivo.close() 
    print("Escritura finalizada")
    return True

def leerBaseDeDatos():
    listaDeVehiculos = []
    archivo = open("baseDeDatos.txt", "r")
    print("Lineas: ")
    for linea in archivo.readlines():
        listaDeValores = linea.split(",")
        print(listaDeValores)
        if listaDeValores[traductorDeBaseDeDatos['clase']] == "Coche":
            listaDeVehiculos.append(Coche(listaDeValores[traductorDeBaseDeDatos['color']],listaDeValores[traductorDeBaseDeDatos['ruedas']],listaDeValores[traductorDeBaseDeDatos['velocidad']],listaDeValores[traductorDeBaseDeDatos['cilindrada']]))
        elif listaDeValores[traductorDeBaseDeDatos['clase']] == "Vehiculo":
            listaDeVehiculos.append(Vehiculo(listaDeValores[traductorDeBaseDeDatos['color']],listaDeValores[traductorDeBaseDeDatos['ruedas']]))
        elif listaDeValores[traductorDeBaseDeDatos['clase']] == "Bicicleta":
            listaDeVehiculos.append(Bicicleta(listaDeValores[traductorDeBaseDeDatos['color']],listaDeValores[traductorDeBaseDeDatos['ruedas']],listaDeValores[traductorDeBaseDeDatos['tipo']]))
    for vehiculo in listaDeVehiculos:
        vehiculo.catalogar()
    archivo.close()
    return listaDeVehiculos
# Crea al menos un objeto de cada subclase
#  y añádelos a una lista llamada vehiculos.
print("Lectura de Base de Datos")
leerBaseDeDatos()
vehiculos = []
resp = True
while resp:
    tipoDeVehiculo = int(input('''Indique el tipo de vehiculo:
    1) Vehiculo
    2) Coche
    3) Bicicleta
    4) Camioneta
    5) Motocicleta'''))

    if tipoDeVehiculo == 1:
        #Vehiculo
        color = input("Indique el color: ")
        ruedas = int(input("Indique cantidad de ruedas"))
        vehiculos.append(Vehiculo(color,ruedas))
    elif tipoDeVehiculo == 2:
        color = input("Indique el color: ")
        ruedas = int(input("Indique cantidad de ruedas"))
        velocidad = float(input("Indique la velocidad"))
        cilindrada = int(input("Inique la cilindrada"))
        vehiculos.append(Coche(color,ruedas,velocidad,cilindrada))
        #Coche
    elif tipoDeVehiculo == 3:
        #Bici
        color = input("Indique el color: ")
        ruedas = int(input("Indique cantidad de ruedas"))
        tipo = -1
        while tipo < 1 or tipo > 2:
            tipo = int(input(''' Indique el tipo:
            1) deportivo
            2) urbana'''))

        if tipo == 1:
            tipo = "deportivo"
        else:
            tipo = "urbana"
        vehiculos.append(Bicicleta(color,ruedas,tipo))
    elif tipoDeVehiculo == 4:
        #Camioneta
        print("Camioneta aun no esta implementado")
    elif tipoDeVehiculo == 5:
        #Moticicleta
        print("Motocicleta aun no esta implementado")
    else:
        print("Tipo Inexistente")

    respuesta = int(input("Ingrese 1 si desea continuar o 0 para ver la lista de vehiculos"))
    if respuesta == 1:
        resp = True
    else:
        resp = False

escribirBaseDeDatos(vehiculos)
# el tipo de acceso w es para sobreescribir el contenido
#del archivo
