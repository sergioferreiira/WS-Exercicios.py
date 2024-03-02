class Pessoa:
    def dirige(self, carro):
        carro.acelera()
        carro.freia()
        
        
class Carro:
    def acelera(self):
        print('acelerando')
        
    def freia(self):
        print('freia')
        

p = Pessoa()
c = Carro()

# p.dirige(c)

print(c)