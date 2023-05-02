# 1
import random
class Dado():
    def __init__(self,faces ):
        self.faces= faces
    def rolar(self):
        return random.randint(1,self.faces)
d6= Dado(6)
for i in range(3):
    print(d6.rolar())    
d8= Dado(8)
print('Dado de 8 faces')
for i in range(3):
     print(d8.rolar())
d12= Dado(12)
print('Dado de 12 faces')
for i in range(3):
    print(d12.rolar())    
# 2
# class Calculadora()
# 3
class Cliente():
    def __init__(self,nome,sobrenome,dataDeNacimento,email,cpf,senha,bloqueado):
        self.nome= ''
        self.sobrenome=''
        self.dataDeNacimento=''
        self.email=''
        self.cpf=''
        self.senha=''
        self.bloqueado= False
    def setNome(self, nome):
        self.nome=nome
    def setSobrenome(self,sobrenome):
        self.sobrenome=sobrenome
    def setDataDeNacimento(self,dataDeNacimento):
        self.dataDeNacimento= dataDeNacimento
    def setcpf(self,cpf):
        if len(cpf)>11:
            self.cpf= cpf
        else:
            self.cpf=cpf
    def setsenha(self, senha):
        self.senha                

