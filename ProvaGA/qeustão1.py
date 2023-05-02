class Bioma():
    def __init__(self,nome,fauna, flora):
        self._nome= nome
        self._fauna= fauna
        self._flora= flora
    def get_nome(self):
        return self.nome
    def adicinaAnimal(self, Animal):
        faunaBR.append(Animal)
        return faunaBR
    def adicinaplata(self,Planta):
        floraBR.append(Planta)
        return floraBR  
    def exibefauna(self,faunaBR):
        for i in range(len(floraBR)):
            for j in range(len(floraBR[i])):
                print(floraBR[i][j], end=' ') 
    def exibeflora(self,floraBR):
        for i in range(len(floraBR)):
            for j in range(len(floraBR[i])):
                print(floraBR[i][j], end=' ')

class Animal():
    def __init__(self, nome, nomecientifico,filo, classe, familia,genero,especie,estadoDeConservacao):
        self._nome=nome
        self._nomecientifico= nomecientifico
        self._filo= filo
        self._classe= classe
        self._familia=familia
        self._genero=genero
        self._especie= especie
        self._estadoDeConservacao= estadoDeConservacao
    def get_nome(self):
            return self._nome    
class Vegetal():
    def __init__(self,nome, nomecientifico,filo, classe, familia,genero,especie,estadoDeConservacao):
        self._nome=nome
        self._nomecientifico= nomecientifico
        self._filo= filo
        self._classe= classe
        self._familia=familia
        self._genero=genero
        self._especie= especie
        self._estadoDeConservacao= estadoDeConservacao                 
    def get_nome(self):
        return self._nome             

faunaBR = [
    # [Animal	Amazônia Mata_Atlântica	Cerrado	Caatinga Pampa	Pantanal]
    ['Capivara',	True,	True,	True,	True,	True,	True],
    ['Gralha azul',	False,	True,	False,	False,	True,	False],
    ['Tamanduá-bandeira',	True,	True,	True,	False,	True,	False],
    ['Onça pintada',	True,	True,	False,	True,	False,	True],
    ['Tatu-bola',	False,	False,	False,	True,	False,	False]
]
   
floraBR = [
    # [Planta	Amazônia Mata_Atlântica	Cerrado	Caatinga Pampa	Pantanal]
    ['Ipê amarelo',	True,	True,	True,	True,	True,	True],
    ['Araucária',	False,	True,	False,	False,	True,	False],
    ['Mandacaru',	False,	False,	True,	True,	False,	False],
    ['Vitória-régia',	True,	False,	False,	False,	False,	True],
    ['Jatobá',	True,	True,	True,	False,	False,	True]

]

amazonia= Bioma('amazonia','','')
mata_atlantica= Bioma('Mata-Atlantica','','')
catinga= Bioma('Catinga','','')
cerrado= Bioma('Cerrado','','')
pampa= Bioma('Pampa','','')
pantanal=Bioma('Pantanal','','')
amazonia.adicinaAnimal(faunaBR,Animal)

# for i in range(len(faunaBR)):
#     for j in range(len(faunaBR[i])):
#         print(faunaBR[i][j], end=' ')
#         # if i==0 and j==0:
#         #    animal1= Animal('capivara','','','','','','','')
#         # elif i==0 and j==1:
#         #    animla2= Animal('gralha azul','','','','','','','')
#         # elif i==0 and j==2:
#         #    animal3 = Animal('Tamabua-bandeira','','','','','','','')
#         # elif i==0 and j==3:
#         #    animal4= Animal('onça pintada','','','','','','','')
#         # elif i==0 and j==4:
#         #    animal5= Animal('Tatu-Bola','','','','','','','')
    # print('\n')

        
for i in range(len(floraBR)):
    for j in range(len(floraBR[i])):
        print(floraBR[i][j], end=' ')
        if i==0 and j==0:
           vegetal1= Vegetal('ipe-amarelo','','','','','','','')
        elif i==0 and j==1:
           vegetal2=Vegetal('araucaria','','','','','','','')
        elif i==0 and j==2:
           vegetal3 = Vegetal('mandacaru','','','','','','','')
        elif i==0 and j==3:
            vegetal4= Vegetal('Vitoria-Regia','','','','','','','')
        elif i==0 and j==4:
          vegetal5 = Vegetal('Jatoba','','','','','','','')
    print('\n')

# print(animal1.get_nome())
print(vegetal4.get_nome())
biomas=[amazonia, mata_atlantica,catinga, cerrado, pampa,pantanal]
for i in range(len(biomas)):
    print(i)
    if i == 0:
        # amazonia.adicinaAnimal(animal1)
        # amazonia.adicinaAnimal(animal3)
        # amazonia.adicinaAnimal(animal4)
        amazonia.adicinaplata(vegetal1)
        amazonia.adicinaplata(vegetal4)
        amazonia.adicinaplata(vegetal5)
    elif i==1:
        # mata_atlantica.adicinaAnimal(animal1)
        # mata_atlantica.adicinaAnimal(animal2)
        # mata_atlantica.adicinaAnimal(animal3)
        # mata_atlantica.adicinaAnimal(animal4)  
        mata_atlantica.adicinaplata(vegetal1)
        mata_atlantica.adicinaplata(vegetal2)
        mata_atlantica.adicinaplata(vegetal5)
    elif i==2:
        # catinga.adicinaAnimal(animal1)
        # catinga.adicinaAnimal(animal4)
        # catinga.adicinaAnimal(animal5)
        catinga.adicinaplata(vegetal1)
        catinga.adicinaplata(vegetal3)
    elif i==3:
        # cerrado.adicinaAnimala(animal1)
        # cerrado.adicinaAnimal(animal3)
        cerrado.adicinaplata(vegetal1)
        cerrado.adicinaplata(vegetal3)
        cerrado.adicinaplata(vegetal5)
    elif i== 4:
        pampa.adicinaplata(vegetal1)
        pampa.adicinaplata(vegetal2)
        # pampa.adicinaAnimal(animal1)
        # pampa.adicinaAnimal(animal2)
        # pampa.adicinaAnimal(animal3)
    elif i== 5:
        # pantanal.adicinaAnimal(animal1)          
        # pantanal.adicinaAnimal(animal2)
        pantanal.adicinaplata(vegetal1)
        pantanal.adicinaplata(vegetal4)
        pantanal.adicinaplata(vegetal5)
amazonia.exibeflora(floraBR)    
pantanal.exibefauna(faunaBR)   