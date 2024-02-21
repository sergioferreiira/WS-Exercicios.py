'''
Exercício 1: Criar uma Classe com @property
Crie uma classe chamada Person que tenha os atributos name e age. 
Utilize o decorator @property para criar métodos de acesso apenas leitura para esses atributos.

'''

class Person:
    def __init__(self):
        self._name = None
        self._age = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            raise('O numero digitado é negativo')
        


p1 = Person()

p1.name = 'Sergio'
p1.age = 25

print(p1.name, p1.age)

