from itertools import combinations


class Quadrados(object):
    def __init__(self, com, fim):
        self.com = com
        self.fim = fim
        
    def __iter__(self):
        return self
    def __next__(self):
        if self.com < self.fim:
            self.com += 1
            return self.com ** 2
        else:
            raise StopIteration
        
        
    
    
x = Quadrados(0, 5)

print(x)


print(iter(x) is x)

for i in x:
    print(i)
    
#Quais as vantagens de ter o próprio objeto iterador

#list(x) retorna []


y = Quadrados(0, 5)


list(y)

#modificação


class Quadrados_iter(object):
    def __init__(self, com, fim):
        self.com = com
        self.fim = fim
        
        
    def __next__(self):
        if self.com < self.fim:
            self.com += 1
            return self.com ** 2
        else:
            raise StopIteration

class Quadrados(object):
    def __init__(self, com, fim):
        self.com = com
        self.fim = fim
        
    def __iter__(self):
        return Quadrados_iter(self.com, self.fim)
    
    


class QuadradosComYield(object):
    def __init__(self, com, fim):
        self.com = com
        self.fim = fim
        
    def __iter__(self):
        for i in range(self.com + 1, self.fim + 1):
            yield i ** 2
            
            
teste = QuadradosComYield(0, 5)

for i in teste:
    print(i)