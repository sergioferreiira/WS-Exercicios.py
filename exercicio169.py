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



nomes = ['Salvador', 'Ubatuba', 'Belo Horizonte']
valores = ['BA', 'SP', 'MG', 'RJ']

nova_lista_atualizada = []


def zipper(x):
    def unir_valores(y):
        uniao = zip(x ,y)
        resultado = list(uniao)
        return resultado
    return unir_valores


passar_zipper = zipper(nomes)
uniao_do_nome_uf = passar_zipper(valores)

print(uniao_do_nome_uf)





