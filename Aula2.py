class Mago:
    def __init__(self, nome, idade, escola):
        self.nome= nome
        self.idade= idade
        self.escola= escola

    def andar(self):
        print('estou andando')

    def falar (self):
        print('Ola amigo! Meu nome é ', self.nome)

    def invocarMagia():
        print('estou invocando magia')         

hp= Mago('Harry Potter', 17, 'Hogwarts')
dm = Mago('Draco Malfoy', 18, 'Hogwarts')

asp= Mago('Alvo Severo Potter',13, "Hogwarts")

print(asp.nome)
print(dm.idade)
print(hp.escola)