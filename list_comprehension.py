import random

#Forma compacta de criar uma lista

l = [x + 10 for x in range(10)]


#Exatamente a mesma coisa

l_exp = []

for i in range(10):
    l_exp.append(i+10)
    

#Constitui-se em:
#Uma expressão  x+10
#Um for loop for x in range(10)
#Um objeto iterável range(10)

#Tentativa de se equiparar a velocidade do c

#A maioria dos exemplos de uso é na leitura de arquivos

l = None

try:    
    a = open('ex.py', 'a')
    a.write('caquinha')
except IOError:
    print('Oops, fiz caquinha!')
finally:
    a.close()
    
a = open('ex.py', 'r')
l = a.readlines()

print(l)

#l = [l.rstrip('\n') for linha in l]

#Elimina todos as \n do arquivo

a.close()

#É mais eficiente em memória e processamento

#Gera uma lista com números aleatório entre 1 e 30
l = [random.randint(1, 30) for i in range(30) if i % 2 == 0]

#Gera uma lista de números pares

l = [x for x in range(30) if x % 2 == 0]


#nested for loops
#Mas não recomendável utilizar muitos nested for loops, porque vc acaba perdendo eficiência
#devido ao aumento de complexidade


new = [x + y for x in 'abc' for y in 'lmn']


print(new)