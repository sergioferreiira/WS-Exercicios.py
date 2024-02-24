# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno

class A:
    def __init__(self, valor):
        self.valor = valor

    def metodo(self):
        print('sou A')

class B(A):
    def __init__(self, valor , teste):
        super().__init__(valor)
        self.teste = teste

    def metodo(self):
        print('sou b')


class C(B):
    def metodo(self):
        super(B , self).metodo()
        super().metodo()
        print('sou c')
        print(f'esse e o parametro do init do A {self.valor} esse e o da class B {self.teste}') 


c1 = C(1 , 'teste')

c1.metodo()