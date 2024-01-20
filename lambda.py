# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)


# #######APRESENTAÇÃO DE LAMBDA ###################


# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]


# def exibir(lista):
#     for lista in lista:
#         print(lista)
#     print()

# l1 = sorted(lista, key= lambda item: item['nome'])
# l2 = sorted(lista, key= lambda item: item['sobrenome'])

# exibir(l1)
# exibir(l2)

###################################################

def multiplicar(funcao, *args):
    return funcao(*args)

multiplica = multiplicar(
    lambda multiplicador: lambda numero: f'voce está multiplicando o numero {numero} por {multiplicador} usando lambda' , 2
)

for n in lista_multiplicadores:
    print(multiplica(n))