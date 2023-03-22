class Data:
    def __init__(self, dia, mes, ano):
        self.dia= dia
        self.mes= mes
        self.ano= ano

    def imprimeData(self):
        print(self.dia,'/',self.mes,'/',self.ano)

    def impimeDataPorExtenssso(self, cidade):
        # ano= ['Mil','Dois Mil','Tres Mil']
        # ano1=['Cem','Duzentos','Trezentos','Quatrossentos','Quinhentos', 'Seissentos', 'Setesentos', 'Oiticentos', 'Novecentos']
        messes= ['janeiro','fevereiro','março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro' ,'novembro' ,'dezembro']
        messes_por_extensso= messes[self.mes-1]
        print( cidade ,self.dia,',',messes_por_extensso,',',self.ano)

d= Data(20,2,2004)
d.imprimeData()
d.impimeDataPorExtenssso('São Leopoldo')