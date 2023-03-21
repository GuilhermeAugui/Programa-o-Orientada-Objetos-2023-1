class Data:
    def __init__(self, dia, mes, ano):
        self.dia= dia
        self.mes= mes
        self.ano= ano

    def imprimeData(self):
        print(self.dia,'/',self.mes,'/',self.ano)

    def impimeDataPorExtenssso(self, cidade):
        messes= ['janeiro','fevereiro','março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro' ,'novembro' ,'dezembro']
        messes_por_extensso= messes[self.mes-1]
        print(self.dia,'/',self.mes,'/',self.ano)

d= Data(20,2,2004)
d.imprimeData()
d.impimeDataPorExtenssso('São Leopoldo')