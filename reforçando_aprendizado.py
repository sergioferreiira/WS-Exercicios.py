# EMPACOTAMENTO

# def multiplicar(*args):
#     valor_multiplicar = 3
#     for args in args:
#         print(args * valor_multiplicar)
        
# multiplicar(1,2,3,4,5,6,7,8,9,10)


# DESEMPACOTAMENTO

# lista = (1,2,3,4,5,6,7,8,9,10)

# print(*lista, sep="\n")

# EMPACOTAMENTO DE NOMEADOS / # DESEMPACOTAMENTO DE NOMEADOS

# def mostro_valores(**args):
#     dicionario = {**args}
#     print(dicionario)

# mostro_valores( 
#     pessoa1='sergio', 
#     idade=24, 
#     altura=1.7, 
#     peso=90
# )

# desempacotar = {
#     'pessoa': 'sergio',
#     'idade': 24,
#     'altura': 1.7,
#     'peso': 90
# }

# def mostro_desempacotado_kwargs(**kwargs):
#     for chave, valor in kwargs.items():
#         print(chave, valor)

# mostro_desempacotado_kwargs(**desempacotar)


produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    produto
    for produto in produtos
]

print(*novos_produtos , sep='\n')

# lista = [1,2,3,4,5]

# novalista = []

# for n in lista:
#     resultado = n * 2
#     novalista.append(resultado)

# print(novalista)