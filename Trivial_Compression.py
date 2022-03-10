
class CompressedGene(object):
    def __init__(self, gene:str) -> None:
        #Python não tem o conceito de métodos ou variáveis realmente privados
        #Todas as variáveis e métodos podem ser acessados por meio de reflexão
        #Um underscore na frente é usado como convenção para sinalizar que atores externos
        #à classe não deverão depender da implementação de um método
        self._compress(gene)
        
    def _compress(self, gene:str) -> None:
        self.bit_string:int = 1
        
        print(self.bit_string << 2)
        
        
        
        #0x00000001 1
        
        #0x00000010  2
        
        #0x00000100 3
        
        
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            
           
            #sentinel
            
            if nucleotide  == 'A':
                self.bit_string |= 0b00
            elif nucleotide == 'C':
                self.bit_string |= 0b01
            elif nucleotide == 'G':
                self.bit_string |= 0b10
            elif nucleotide == 'T':
                self.bit_string |= 0b11
            else:
                raise ValueError('Invalid nucleotide: {}'.format(nucleotide))
            
    def decompress(self) ->str:
        gene: str = ''
        for i in range(0, self.bit_string.bit_length -1, 2):
            bits: int = self.bit_string >> i &0b11 #obtém apenas 2 bits relevantes
            
            if bits == 0b00:
                gene += 'A'
            elif bits == 0b01:
                gene += 'C'
            elif bits == 0b10:
                gene += 'G'
            elif bits == 0b11:
                gene += 'T'
            else:
                raise ValueError('Invalid bits:{}'.format(bits))
            
    def __str__(self) -> str:
        return self.decompress()
    
    
    
if __name__ == '__main__':
    from sys import getsizeof
    
    original: str = 'TGGGAAAAGGGAATGAGGGTACCCC'*10
    
    print('Original is {} bytes'.format(getsizeof(original)))
    
    compressed: CompressedGene = CompressedGene(original)

    print('Compressed is {} bytes'.format(getsizeof(compressed.bit_string)))
                
    