# Exercício - Unir listas

# Crie uma função zipper
# O trabalho dessa função será unir duas
# listas na ordem.

# Use todos os valores da menor lista.

# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']

# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

import copy

citys = ['Salvador', 'Ubatuba', 'Belo Horizonte']
uf = ['BA', 'SP', 'MG', 'RJ']

nova_cidade = copy.deepcopy(citys)
nova_uf = copy.deepcopy(uf)


novo_dicionario = {}

# def zipper(*args ,**kwargs):
#     print(*args)
#     def unir_uf(*ufs):
#         for cidade in args:
#             a = cidade
#         return a
#     return 

# executa_funcao = zipper(dict_de_cidades)
# estados = executa_funcao(uf)

# print(estados)


