
calc_strike = lambda x, y: x-y 

class Personagem(object):
    def __init__(self, nome, idade, habilidades):
        self.nome = nome
        self.idade = idade
        self.habilidades = habilidades
        
    def __str__(self):
        return '%s tem %i de idadee uma forca de %i'%(self.nome, self.idade, self.habilidades['forca'])
    
    

class Aventureiro(Personagem):
        def __init__(self, nome, idade, habilidades):
            super().__init__(nome, idade, habilidades)
            pass
        


class Inimigo(Personagem):
    def __init__(self, nome, idade, habilidades):
        super().__init__(nome, idade, habilidades)
        pass

    
        
adv = Aventureiro('lucas', 123, habilidades = {'forca': 332})
ene = Inimigo('ogro', 1000, habilidades={'forca': 23})

#Erro de asserção
#Valor1 não é maior que valor2
assert adv.habilidades['forca'] > ene.habilidades['forca']

#calc_strike retorna a referência de memória da função anônima
res = calc_strike(adv.habilidades['forca'], ene.habilidades['forca']) 

print(res)