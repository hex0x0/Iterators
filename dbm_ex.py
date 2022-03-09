import dbm


class EntradaErro(Exception):
    def __init__(self, entrada):
        self.entrada = entrada
        
        
    def VerificaErro(self):
        divisao = self.entrada.split('.')
        
        try:
        
            if not (divisao[0] == 'www' and divisao[2] == 'com' and divisao[3] == 'org'):
                raise self
        except IndexError:
            raise self
        else:
            return self.entrada
    
    def __str__(self):
            return 'A entrada %s nao eh valida'%self.entrada
      
      
 
        
class Manipula(object):
    def __init__(self, db):
        self.db = db
        self.main()
        
        
    def colocaValorDic(self):
        nome = input('Digite o nome do site: ').lower()
        
    
        entrada  = EntradaErro(input('Digite o site')).VerificaErro()
        
        self.db[nome] = entrada
        
        
    def abreEssaBudega(self):
        #Retorna site no formato de bytes
        nome = input('Digite nome:').lower()
        
        for key in self.db:
            if nome == key.decode():
                print(self.db[nome].decode())
    
    def select_options(self):
        while True:
            cmd = input('Digite i para inserir ou  a para abrir ou q para sair\n').lower()
            
            if not cmd.isalpha():
                print('Só letras')
            elif cmd.startswith('i') or cmd.startswith('a') or cmd.startswith('q'):
                return cmd
            else:
                print('Entrada invalida')
    
    def main(self):
        
        while True:
            cmd = self.select_options()
        
            if cmd.startswith('i'):
                self.colocaValorDic()
            elif cmd.startswith('a'):
                self.abreEssaBudega()
            else:
                break       

    
bytes_file = dbm.open('fodase.fod', 'c')
    
bytes_file['porno'] = 'www.xvideos.com'
    
print(bytes_file)
    
for key in bytes_file:
    if 'porno' == key.decode():
        print(bytes_file[key].decode())
            
            
if __name__ == '__main__':
    try:
        #tenta abrir o banco
        db = dbm.open('x', 'c')
    except IOError:
        print('Erro ao tentar abrir')
    else:
        Manipula(db)