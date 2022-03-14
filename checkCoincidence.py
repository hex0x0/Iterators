#checar validade de senha numerica



import random 



favoraveis:int = 0

l = [random.randint(1, 366) for i in range(1000)]



def checkCoincidence(l):
    resp = [True for i in l if l.count(i) > 1]

    if len(resp) > 0:
        return True
    else:
        return False
    


for i in range(1000):
    if checkCoincidence:
        favoraveis += 1


print(favoraveis)


