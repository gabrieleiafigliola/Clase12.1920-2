#from random import random
from random import randint

estudiantes = [
{'ID':  1	, 'Cedula': 27342497	,'Carnet': 20181110540	,'Nombre': 'Andújar	Diego'},
{'ID':  2, 'Cedula': 27903902,'Carnet': 20191110255,'Nombre': 'BlancoJhoel'},
{'ID':  3, 'Cedula': 28155110,'Carnet': 20191110217,'Nombre': 'CaceresRicardo'},
{'ID':  4, 'Cedula': 26367170,'Carnet': 20171110246,'Nombre': 'De NobregaDaniela'},
{'ID':  5, 'Cedula': 27584709,'Carnet': 20181110345,'Nombre': 'DorazioSebastian'},
{'ID':  6, 'Cedula': 26213731,'Carnet': 20201120141,'Nombre': 'DávilaKaren'},
{'ID':  7, 'Cedula': 26618946,'Carnet': 20191120001,'Nombre': 'Fernandez Ezequiel'},
{'ID':  8, 'Cedula': 28012309,'Carnet': 20191110679,'Nombre': 'FerrerMaria'},
{'ID':  9, 'Cedula': 27796470,'Carnet': 20191110102,'Nombre': 'GonzálezOriana'},
{'ID': 10, 'Cedula': 27625330,'Carnet': 20191110345,'Nombre': 'GuzmànAlejandro'},
{'ID': 11, 'Cedula': 25641379,'Carnet': 20161110457,'Nombre': 'HanKevin   '},
{'ID': 12, 'Cedula': 25736710,'Carnet': 20161110446,'Nombre': 'HernandezKevin'},
{'ID': 13, 'Cedula': 27625290,'Carnet': 20181120009,'Nombre': 'PerestreloLeandro'},
{'ID': 14, 'Cedula': 26510325,'Carnet': 20171110107,'Nombre': 'RieraFabrizio'},
{'ID': 15, 'Cedula': 27773794,'Carnet': 20171110713,'Nombre': 'RiveraLuis'},
{'ID': 16, 'Cedula': 27039353,'Carnet': 20181110159,'Nombre': 'RodriguezDiego'},
{'ID': 17, 'Cedula': 27670424,'Carnet': 20191110211,'Nombre': 'RodriguezRoy'},
{'ID': 18, 'Cedula': 26946135,'Carnet': 20181110110,'Nombre': 'RomeroAndrés'},
{'ID': 19, 'Cedula': 27624205,'Carnet': 20191110141,'Nombre': 'RujanaValeria'},
{'ID': 20, 'Cedula': 28324864,'Carnet': 20191110700,'Nombre': 'SancioMatteo'},
{'ID': 21, 'Cedula': 26989156,'Carnet': 20181110648,'Nombre': 'SosaGuillermo'},
{'ID': 22, 'Cedula': 27769576,'Carnet': 20191110851,'Nombre': 'StanislaoLuis'},
{'ID': 23, 'Cedula': 28158047,'Carnet': 20191110561,'Nombre': 'TezaraAngélica'},
{'ID': 24, 'Cedula': 25663228,'Carnet': 20141110280,'Nombre': 'ThielenManuel'},
{'ID': 25, 'Cedula': 27392553,'Carnet': 20161110690,'Nombre': 'VargasDaniel'},
{'ID': 26, 'Cedula': 27040051,'Carnet': 20181110664,'Nombre': 'VicensEduardo'}
]

estudiantesDictionary = {
'1': { 'Cedula': 27342497	,'Carnet': 20181110540	,'Nombre': 'Andújar	Diego	    '},
'2': { 'Cedula': 27903902	,'Carnet': 20191110255	,'Nombre': 'Blanco	Jhoel	    '},		
'3': { 'Cedula': 28155110	,'Carnet': 20191110217	,'Nombre': 'Caceres	Ricardo	    '},		
'4': { 'Cedula': 26367170	,'Carnet': 20171110246	,'Nombre': 'De Nobrega	Daniela	'},		
'5': { 'Cedula': 27584709	,'Carnet': 20181110345	,'Nombre': 'Dorazio	Sebastian	'},	
'6': { 'Cedula': 26213731	,'Carnet': 20201120141	,'Nombre': 'Dávila	Karen	    '},		
'7': { 'Cedula': 26618946	,'Carnet': 20191120001	,'Nombre': 'Fernandez Ezequiel	'},		
'8': { 'Cedula': 28012309	,'Carnet': 20191110679	,'Nombre': 'Ferrer	Maria	    '},
'9': { 'Cedula': 27796470	,'Carnet': 20191110102	,'Nombre': 'González	Oriana	'},	
'10': { 'Cedula': 27625330	,'Carnet': 20191110345	,'Nombre': 'Guzmàn	Alejandro	'},
'11': { 'Cedula': 25641379	,'Carnet': 20161110457	,'Nombre': 'Han	Kevin	       	'},
'12': { 'Cedula': 25736710	,'Carnet': 20161110446	,'Nombre': 'Hernandez	Kevin	'},		
'13': { 'Cedula': 27625290	,'Carnet': 20181120009	,'Nombre': 'Perestrelo	Leandro	'},
'14': { 'Cedula': 26510325	,'Carnet': 20171110107	,'Nombre': 'Riera	Fabrizio	'},	
'15': { 'Cedula': 27773794	,'Carnet': 20171110713	,'Nombre': 'Rivera	Luis	    '},
'16': { 'Cedula': 27039353	,'Carnet': 20181110159	,'Nombre': 'Rodriguez	Diego	'},
'17': { 'Cedula': 27670424	,'Carnet': 20191110211	,'Nombre': 'Rodriguez	Roy	    '},
'18': { 'Cedula': 26946135	,'Carnet': 20181110110	,'Nombre': 'Romero	Andrés	    '},	
'19': { 'Cedula': 27624205	,'Carnet': 20191110141	,'Nombre': 'Rujana	Valeria	    '},	
'20': { 'Cedula': 28324864	,'Carnet': 20191110700	,'Nombre': 'Sancio	Matteo	    '},		
'21': { 'Cedula': 26989156	,'Carnet': 20181110648	,'Nombre': 'Sosa	Guillermo	'},	
'22': { 'Cedula': 27769576	,'Carnet': 20191110851	,'Nombre': 'Stanislao	Luis	'},	
'23': { 'Cedula': 28158047	,'Carnet': 20191110561	,'Nombre': 'Tezara	Angélica	'},	
'24': { 'Cedula': 25663228	,'Carnet': 20141110280	,'Nombre': 'Thielen	Manuel	    '},	
'25': { 'Cedula': 27392553	,'Carnet': 20161110690	,'Nombre': 'Vargas	Daniel	    '},	
'26': { 'Cedula': 27040051	,'Carnet': 20181110664	,'Nombre': 'Vicens	Eduardo	    '}	
}

index = randint(1, 27)
print("Index",index)
print("Index2",str(index))
print(estudiantes[index-1])
print(estudiantesDictionary[str(index)])