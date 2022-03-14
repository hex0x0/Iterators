import pickle


with open('listas.obj', 'rb') as arq:
   gastos =  pickle.load(arq)
   
   gastos_corr = pickle.load(arq)


corr = list(map((lambda x: gastos_corr[x] - gastos[x]), range(len(gastos))))


lmt = 1500.0

filtrado = list(filter((lambda x: x <= lmt), corr))


print(filtrado)