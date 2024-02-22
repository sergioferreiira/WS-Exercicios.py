# class Carro:
#     def __init__(self, nome, motor , fabricante):
#         self.nome = nome
#         self._motor = motor
#         self._fabricante = fabricante

#     def caracteristicasCarro(self):
#         return f'O nome do carro é {self.nome} com um motor de potencia {self._motor} e fabricado por {self._fabricante}'
        
# class Motor:
#     def __init__(self, nome):
#         self.nome = nome

# class Fabricante:
#     def __init__(self, nome):
#         self.nome = nome


# motor_opala = Motor('V12')
# fabricante_opala = Fabricante('MotorCustons')
# opala = Carro('Opala', motor_opala.nome , fabricante_opala.nome) 


# print(opala.caracteristicasCarro())


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


    def caracteristicasCarro(self):
        motor_nome = self._motor.nome if self._motor else 'sem motor'
        fabricante_nome = self._fabricante.nome if self.fabricante else 'Sem fabricante'
        print(f'O nome do carro é {self.nome} com um motor de potencia {motor_nome} e fabricado por {fabricante_nome}')
        
class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome


opala = Carro('Opala') 
opala._motor = Motor('V12')
opala._fabricante = Fabricante('MotorCustons')

print(opala.caracteristicasCarro())