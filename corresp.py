import pickle

percentual = float(input('Digite percentual a mudar: '))

v_perc = percentual / 100

v_perc_corr = v_perc + 1


gastos = list(map((lambda x: float(x)), open('gastos.txt')))

gastos_corrigidos = list(map((lambda x: x*v_perc_corr), gastos))


with open('lista_corrigida.txt', 'w') as arq:
    for g in gastos_corrigidos:
        arq.write('%.2f'%g+'\n')


#guarda listas

with open('listas.obj', 'wb') as arq:
    pickle.dump(gastos, arq)
    pickle.dump(gastos_corrigidos, arq)


    
    
