"""


@Lucas

Created: 09/03/2022

This file is only for education purposes. This did not intend to be an accurate example of my knowledge 
on the subject 




"""
arq = open('arq.txt', 'w')
arq.write('lucas\n')
arq.write('pedro\n')
arq.write('jose\n')

arq.close()

arq = open('arq.txt')



print(arq.__next__())


y = open('arq.txt').readlines()

#Y é um objeto iterável, mas não iterador (iterator)

z = y.__iter__()

z.__next__()

#segunda parte

lista_iteravel = iter(arq)

while True:
    try:
        ele = next(lista_iteravel)
    except StopIteration:
        break
    

#terceira parte

n = enumerate('abc')


for i in n:
    print(i)


#Cria uma tupla dos valores de forma numerada

#Existem também outros objetos iteráveis 

l1 = [1, 2, 3]
l2 = [4, 5, 6]

zipped_obj = zip(l1, l2)    
#Zip nos devolve o objeto iterável do tipo zip
print(zipped_obj)


recebe_lista = list(zipped_obj)

print(recebe_lista)


produtos = ['presunto', 'queijo', 'pao']
precos = [1, 2, 3]

combinacao = zip(produtos, precos)

obj_dict_created_for_combinacao = dict(combinacao)

print(obj_dict_created_for_combinacao)

#Se você quiser saber se combinação é um objeto iterável, basta fazer:

if combinacao is combinacao.__iter__():
    print('É o próprio __iter__')



#O map é muito similar a uma list comprehension

#map(object)
#  map(func, *iterables)
#

#Com um argumento
map_ex = map((lambda x: x**2), range(4))

print(list(map_ex))

#Com dois argumentos
map_ex_two_arguments = map((lambda x, y: x*y), range(4), range(4))

print(list(map_ex_two_arguments))


#Não necessariamente precisa ser uma função anônima


def soma(x, y):
    return x + y


map_regular_function = map(soma, range(4), range(4))

#List comprehension > map

#Filter
#
#
#

#Se voce fizer o seguinte 

def retornaPar(x):
    if x % 2 == 0:
        return x
    
    
par = [retornaPar(x) for x in range(3)]
#retorna 0, None, 2
print(par)

map_par = map(retornaPar, range(3))

#print(map_par)

#
#   filter(function or nothing, iterable)
#

a = filter((lambda x: x%2 == 0), range(5))

print(list(a))

#magic


map_filter = map((lambda x: x ** 2), filter((lambda x: x % 2 == 0), range(5)))

print(list(map_filter))