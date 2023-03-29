# 1
# import random
# class Dado():
#     def __init__(self,faces ):
#         self.faces= faces
#     def rolar(self):
#         return random.randint(1,self.faces)
# d6= Dado(6)
# for i in range(3):
#     print(d6.rolar())    
# d8= Dado(8)
# print('Dado de 8 faces')
# for i in range(3):
#      print(d8.rolar())
# d12= Dado(12)
# print('Dado de 12 faces')
# for i in range(3):
#     print(d12.rolar())    
#2
class Cauladora():
    def __init__(self, numero1, numero2):
        self.numero1= numero1
        self.numero2= numero2
    def soma(self, numero1, numero2):
        resultado= numero1+numero2
        print(resultado)
    def sutracao(self, numero1, numero2):
        resultado= numero1-numero2
        print(resultado)
    def mulpiplicar(seelf, numero1,numero2):
        resultado=numero1*numero2
        print(resultado)   
    def dividir(self,numero1, numero2):
        if numero2 == 0:
            resultado=('-1')
        else:
           resultado= self.numero1/numero2
        print(resultado) 

op1=Cauladora(10,2)
op1.soma(10,2)
       