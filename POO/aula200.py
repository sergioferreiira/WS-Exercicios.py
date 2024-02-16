class Pessoa:
    def __init__(self, nome , sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    

p1 = Pessoa('sergio', 'ferreira')


print(p1.nome +' '+ p1.sobrenome)


'''
    um metodo e uma função que está dentro da classe
'''

class Carro:
    def __init__(self, marca , nome):
        self.marca = marca
        self.nome = nome

    def acelerar(self):
        print(f'O carro {self.nome} da marca {self.marca}, está acelerando!!!!!')
        print("VRUUUUUUMMMMMMMMMM")
        


camaro = Carro('Chevrole' , 'Camaro')

camaro.acelerar()