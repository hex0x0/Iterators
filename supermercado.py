import shelve


def main():
    itens = []
    precos = []
    
    
    for linha in open('super.txt'):
        L = linha.split('-')
        try:
            itens.append(L[0].rstrip())
            precos.append(L[1].rstrip())
        except(ValueError, IndexError):
            break
        
    dtbase = shelve.open('supermarket.db')
    dtbase.update(dict(zip(itens, precos)))
    
    dtbase.close() 

    
        
        