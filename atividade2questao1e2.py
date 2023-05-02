class Mago:
    def __init__(self, nome, idade, escola, casa, apelido):
        self.nome= nome
        self.idade= idade
        self.escola= escola
        self.casa= casa
        self.apelido= apelido
    def andar(self):
        print('estou andando')

    def falar (self):
        print('Ola amigo! Meu nome é ', self.nome)

    def invocarMagia():
        print('estou invocando magia')
    
    def apelidos(self):
        print('Quando estudei lá meu apelido era', self.apelido,'você tem algum já?')
   
    def minhaCasa(self):
        print('Minha casa era', self.casa)

tp= Mago('Tiago, Potter', 28, 'Hogwarts', 'Grifinória', 'Pontas')
rl= Mago('Remo Lupin', 30, 'Hogwarts', 'Grifinória', 'Aluado')
sb= Mago('Sirius Black', 35, 'Hogwarts', 'Grifinória','Almofadinhas')
ss= Mago('Severus Sanape', 45, 'Hogwarts','Sonserina', 'Ranhoso')       
hp= Mago('Harry Potter', 17, 'Hogwarts', 'Grifinória', 'O menino que sobreviveu') 
