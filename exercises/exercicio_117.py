

# def duplica(numero):
#     resultado = numero * 2
#     novonumero = str(numero)
#     x = novonumero + novonumero
#     return resultado , x

# def triplica(numero):
#     resultado = numero * 3
#     novonumero = str(numero)
#     x = novonumero * 3
#     return resultado , x

# def quadruplica(numero):
#     resultado = numero * 4
#     novonumero = str(numero)
#     x = novonumero * 4
#     return resultado , x

# x = duplica(2)
# y = triplica(2)
# z = quadruplica(2)

# print(x, y , z)

#  usando closure

def multiplicacoes(numero):
    def numero_multiplicador(multiplicador):
        return numero * multiplicador
    return numero_multiplicador

numero_a_multiplicar = multiplicacoes(2)

for numero in [ 2 , 3 , 4]:
    print(numero_a_multiplicar(numero))