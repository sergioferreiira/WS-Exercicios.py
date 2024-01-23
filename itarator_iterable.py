# iterable = ['Eu','Progamo','python']
# iterator = iterable.__iter__()


# for i in iterable:
#     print(iterator.__next__())


# class Contador:
#     def __init__(self, limite):
#         self.limite = limite
#         self.valor = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.valor < self.limite:
#             resultado = self.valor
#             self.valor += 1
#             return resultado
#         else:
#             raise StopIteration

# # Exemplo de uso
# contador = Contador(5)
# for numero in contador:
#     print(numero)




######################### generator ################################

def generator(n=0 , maximum=10):
    while True:
        yield n 
        n += 1

        if n > 10:
            return
        
gen = generator(maximum=100)
for n in gen:
    print(n)
    
