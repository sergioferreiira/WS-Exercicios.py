# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:
    def __init__(self, cor):
        self.cor = cor

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor
        
    
c1 = Caneta('azul')

c1.cor = 'preta'

print(c1.cor)


