class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
        
    def inserirPessoaEndereco(self, rua , numero):
        self.enderecos.append(Endereco(rua , numero))
    
    def listarEnderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua , endereco.numero)
        
    def __del__(self):
        print('estou apagando' , self.nome)
        print(f'estou apagando {self.listarEnderecos()}')

class Endereco:
    def __init__(self, rua , numero):
        self.rua = rua
        self.numero = numero
        

p1 = Pessoa('Sergio')
p1.inserirPessoaEndereco('AV brasil', 1234)

print(p1.listarEnderecos())