from struct import *

class RaiseExceptionClass(Exception):
    def __str__(self):
        return ('MANO, BAGULHO É O SEGUINTE: NÃO PODE LETRAS!')
    
    

#Validação rústica, apenas para testes   

rg = '029.950.301-13'


partes = rg.split('.')



primeiro = partes[0]
segundo = partes[1]
terceiro = partes[2].split('-')[0]
ultimo = partes[2].split('-')[1]

"""
if not (len(primeiro) != 3 and len(segundo) != 3 and len(terceiro) != 3 and len(ultimo)!=2):
    raise RaiseExceptionClass()
else:
    print('Tá certo')

"""

num_cpf = int(primeiro + segundo + terceiro + ultimo)


#Refazendo a string para como foi digitada pelo usuário

valor_cpf = num_cpf

str_first = str(valor_cpf % 100)
#13
valor_cpf //= 100



str_secodn = str(valor_cpf % 1000)

#301


valor_cpf //= 1000



str_third = str(valor_cpf % 1000)

#950

valor_cpf //= 1000

str_fourth = str(valor_cpf % 1000)


print('0' + str_fourth + '.' + str_third + '.' + str_secodn + '.' + str_first)

#Final desse trecho








