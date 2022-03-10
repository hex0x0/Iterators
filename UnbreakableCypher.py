from lib2to3.pgen2 import token
from secrets import token_bytes
from typing import Tuple


def random_key(length:int) -> int:
    #gera length bytes aleatórios
    tb:bytes = token_bytes(length)
    
    return int.from_bytes(tb, "big")

#Em python, o operador xor é uma operação bit a bit que devolve false se ambos os operadores forem iguais
#e true se algum deles for diferente
#Um mágica do xor é que você consegue recombinar novamente os valores
#por exemplo: a ^ b = c
# c ^ b = a
# c ^ a = b


def encrypt(original:str) -> Tuple[int, int]:
    original_bytes:bytes  = original.encode()
    
    dummy:int = random_key(len(original_bytes))
    original_key:int = int.from_bytes(original_bytes, "big")
    encrypted:int = original_key ^ dummy
    return dummy, encrypted

    #int.from_bytes() recebe dois argumentos: o primeiro são os bytes que queremos converter para int
    #e o segundo e o endianess (que se refere à ordem dos bytes usada para armazenar os dados)
    
def decrypt(key1:int, key2:int) -> str:
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    
    
    
if __name__ == '__main__':
    key1, key2 = encrypt('One time Pad!')
    
    result: str = decrypt(key1, key2)
    print(result)
    

#Retornou None, devo voltar ao código