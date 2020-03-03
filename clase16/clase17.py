class Vehiculo():

    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def catalogar(self):
        print("Este es un vehiculo con {} ruedas y de tal {} color".format(self.ruedas,self.color))

class Coche(Vehiculo):

    def __init__(self,color,ruedas,velocidad,cilindrada):
        Vehiculo.__init__(self,color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def catalogar(self):
        print("Este es un coche con {} ruedas, de tal {} color, con una velocidad de {} y {} cilindrada".format(self.ruedas,self.color,self.velocidad,self.cilindrada))


class Bibicleta(Vehiculo):
        
    def __init__(self,color,ruedas,tipo):
        Vehiculo.__init__(self,color,ruedas)
        self.tipo = tipo

    def catalogar(self):
        print("Este es una bicicleta con {} ruedas, de color {} y de tipo {}".format(self.ruedas,self.color,self.tipo))

class Camioneta(Coche):

    def __init__(self,color,ruedas,velocidad,cilindrada,carga):
        Coche.__init__(self,color,ruedas,velocidad,cilindrada)
        self.carga = carga

    def catalogar(self):
        print("Este es un camioneta con {} ruedas, de color {} , con una velocidad de {}, {} cilindrada y con una capacidad de carga de {} kg".format(self.ruedas,self.color,self.velocidad,self.cilindrada,self.carga))

class Motocicleta(Bibicleta):

    def __init__(self,color,ruedas,tipo,velocidad,cilindrada):
        Bibicleta.__init__(self,color,ruedas,tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def catalogar(self):
        print("Este es una motocicleta con {} ruedas, de  color {} , con una velocidad de {}, {} cilindrada y de tipo {}".format(self.ruedas,self.color,self.velocidad,self.cilindrada,self.tipo))

# Crea al menos un objeto de cada subclase
#  y añádelos a una lista llamada vehiculos.

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
        vehiculos.append(Bibicleta(color,ruedas,tipo))
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
# vehiculos = []
# vehiculos.append(Vehiculo("Rojo",4))
# vehiculos.append(Coche("Rojo",4,12,8))
# vehiculos.append(Bibicleta("Rojo",2,"deportiva"))
# vehiculos.append(Camioneta("Rojo",4,12,8,100))
# vehiculos.append(Motocicleta("Rojo",2,"deportiva",5,5))

# Realiza una función llamada catalogar() que 
# reciba la lista de vehiculos y los recorra 
# mostrando el nombre de su clase y sus atributos.
print(vehiculos)

for vehiculo in vehiculos:
    print("Tipo: ", type(vehiculo))
    vehiculo.catalogar()
