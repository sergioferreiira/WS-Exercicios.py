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

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-# \/\/ MINHA COMPREENSÃO SOBRE O CONTEUDO \/\/ -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
"""
O LAMBDA e a redução de uma função para uma linha de codigo, assim deixando o codigo menos legivel porem mais curto
um exemplo é:

\/\/\/\/\/\/\/\/ MODO TRADICIONAL
def soma(x , y)
    return x + y

definido a assinatura da função passamos quais serão os parametros de execução da mesma
e retornamos normalmente o tratamento realizado dos parametros

\/\/\/\/\/\/\/\/\/\/\/\/\/  UTILIZANDO LAMBDA
soma = lambda x , y: x + y


no exemplo LAMBDA é utilizado como a assinatura da função e os parametros são passados
fora de seus devidos () e o tratamento dos parametros já é retornado após os : sem 
precisar do return
"""
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-# /\/\ MINHA COMPREENSÃO SOBRE O CONTEUDO /\/\ -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


# ####### APRESENTAÇÃO DE LAMBDA ###################


lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


def exibir(lista):
    for lista in lista:
        print(lista)
    print()

def ordena(x):
    return x['nome']


l1 = sorted(lista, key= ordena)
l2 = sorted(lista, key= lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)

###################################################

# def multiplicar(funcao, *args):
#     return funcao(*args)

# multiplica = multiplicar(
#     lambda multiplicador: lambda numero: f'voce está multiplicando o numero {numero} por {multiplicador} usando lambda' , 2
# )

# for n in lista_multiplicadores:
#     print(multiplica(n))