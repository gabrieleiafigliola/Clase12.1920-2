class MoldeParaGalletas:

    def __init__(self,tam,forma):
        self.tamanio = tam
        self.forma = forma

    def utilizarMolde(self):
        print("Se ha cortado la masa con forma de {} y tamanio de {} cm".format(self.forma,self.tamanio))

    def imprimirDecente(self):
        print("Este es un molde de tamanio {} cm y de forma {}".format(self.tamanio,self.forma))

moldeCorazonGrande = MoldeParaGalletas(5,"Corazon")
moldeCorazonMediano = MoldeParaGalletas(2.5,"Corazon")
#moldeCorazonGrande.imprimirDecente()
#moldeCorazonMediano.imprimirDecente()
moldeTrianguloPequenio = MoldeParaGalletas(1,"triangulo")
# moldeTrianguloPequenio.imprimirDecente()
# moldeCorazonGrande.utilizarMolde()
# moldeCorazonMediano.utilizarMolde()

listaDeMoldes = []
diccionarioDeMoldes = {}
listaDeMoldes.append(moldeCorazonGrande)
diccionarioDeMoldes['CorazonGrande'] = moldeCorazonGrande
listaDeMoldes.append(moldeCorazonMediano)
diccionarioDeMoldes['CorazonMediano'] = moldeCorazonMediano
listaDeMoldes.append(moldeTrianguloPequenio)

print(listaDeMoldes)
for molde in listaDeMoldes:
    molde.imprimirDecente()

for llave in diccionarioDeMoldes:
    diccionarioDeMoldes[llave].imprimirDecente()

print("Que molde desea utilizar?")
for i,molde in enumerate(listaDeMoldes):
        print("ingrese {} si desea utilizar el molde de {} y tamanio {}".format(i,molde.forma,molde.tamanio))
opcion = -1
while opcion < 0 or opcion > 3:
    opcion = int(input())
listaDeMoldes[opcion].imprimirDecente()
# print("Que molde desea utilizar")
# for llave in diccionarioDeMoldes:
#     print("ingres {} si desea utilizar el molde {}".format(llave,llave))

class Persona(object):
    """Clase que representa una Persona"""

    def __init__(self, cedula, nombre, apellido, sexo):
        """Constructor de clase Persona"""
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo

    def __str__(self):
        """Devuelve una cadena representativa de Persona"""
        return "%s: %s, %s %s, %s." % (
            self.__doc__[25:34], str(self.cedula), self.nombre, 
            self.apellido, self.getGenero(self.sexo))

    def hablar(self, mensaje):
        """Mostrar mensaje de saludo de Persona"""
        return mensaje

    def getGenero(self, sexo):
        """Mostrar el genero de la Persona"""
        genero = ('Masculino','Femenino')
        if sexo == "M":
            return genero[0]
        elif sexo == "F":
            return genero[1]
        else:
            return "Desconocido"


class Supervisor(Persona):
    """Clase que representa a un Supervisor"""

    def __init__(self, cedula, nombre, apellido, sexo, rol):
        """Constructor de clase Supervisor"""

        # Invoca al constructor de clase Persona
        Persona.__init__(self, cedula, nombre, apellido, sexo)

        # Nuevos atributos
        self.rol = rol
        self.tareas = ['10','11','12','13']

    def __str__(self):
        """Devuelve una cadena representativa al Supervisor"""
        return "%s: %s %s, rol: '%s', sus tareas: %s." % (
            self.__doc__[26:37], self.nombre, self.apellido, 
            self.rol, self.consulta_tareas())

    def consulta_tareas(self):
        """Mostrar las tareas del Supervisor"""
        return ', '.join(self.tareas)