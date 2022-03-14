import functools
#all, any, sum e reduce
#pega todos os elementos de uma lista pra ver se todos são verdadeiros
algo = all([1, 1, 0, 0, 1, 1])


print(algo)


def all(iterable):
    for element in iterable:
        if not element:
            return False
        
    return True


#any -> verifica se pelo menos um dos elementos é verdadeiro


def any(iterable):
    for element in iterable:
        if element:
            return True
    
    return False


#sum -> soma os elementos de um iterável
#Apenas soma números
#arg_opcional -> valor inicial ao qual outros valores serão somados

#ex  sum([1, 2, 3], arg_opcional)


#Reduce -> Recebe um objeto iterável e combina 
#utiliza uma função pra combinar
#o resultado da função anterior com o elemento seguinte do objeto iterável

def see_sum(x, y):
    print('Adicionado ', x,'a ', y)
    return x + y


#Caiu em desuso por causa do uso generalizado do for loop
print(functools.reduce(see_sum, [1, 2, 3, 4, 5]))


#algoritmo do reduce

def reduce(function, iterable, initializer = None):
    it = iter(iterable)
    
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    
    for element in it:
        value = function(value, element)
        
    return value


