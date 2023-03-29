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
