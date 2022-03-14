#statemet yield {expression}
#economia de memória



def geraQuadrados(n):
    for i in range(n):
        yield i**2
        
        
for i in geraQuadrados(5):
    print(i)
    
 
 
x  = geraQuadrados(5)
#x é o próprio generator

print(x)   

l = list(x)

print(l)

if iter(x) is x:
    print(iter(x))
    
    
for i in [x**2 for x in range(5)]:
    print(i)
    
    
for i in map((lambda x: x** 2), range(5)):
    print(i)
    
    
def novosQuadrados(n):
    l = []
    
    for i in range(n):
        l.append(i**2)
        
    return l


for i in novosQuadrados(5):
    print(i)



def imprime(n):
    for i in range(n):
        x = yield i**2
        print(x)
    
#send é uma forma de enviar mensagem 


x  = imprime(5)

print(x.__next__())


x.send(5)

print(x.__next__()) #Ele fica esperando outro valor de send