class Escritor:

    def __init__(self, nome):
        self.nome = nome
        self.ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta
    

class FerramentaEscritor:
    def __init__(self, nome):
        self.nome = nome

    def escrevendo(self, nomeEscritor):
        return f'O escritor {nomeEscritor} está utilizando a ferramenta {self.nome} para escrever'
    


escritor1 = Escritor('sergio')
caneta = FerramentaEscritor('Caneta Bic')
escritor1.ferramenta = caneta
print(escritor1.ferramenta.escrevendo(escritor1.nome))
