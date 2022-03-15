#um pouco parecido com list comprenhesion
#notação ()

#devolve um objeto gerador

l = (x**2 for x in range(4))


#lista é um objeto iterável, mas não um objeto iterador

#no list os inteiros são jogados na memória
#agora com o objeto gerador, temos o alocamento de memória apenas para a função

#programa simples que gera todas as permutações de uma palavra

#  ano = [ano, noa, nao, oan, aon, ona]
#   permutation = pn, k  = n ! / (n - k) !
#
#
#