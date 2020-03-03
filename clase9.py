class MoldeParaGalletas:

    def __init__(self,tam,forma):
        self.tamanio = tam
        self.forma = forma

    # def __init__(self,tam,forma,nombreOpcional):
    #     self.tamanio = tam
    #     self.forma = forma
    #     self.nombreOpcional = nombreOpcional

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