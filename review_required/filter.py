def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()


produtos = [
    {'nome' : 'Produto 1' , 'preco' : 12.30},
    {'nome' : 'Produto 5' , 'preco' : 7.00},
    {'nome' : 'Produto 3' , 'preco' : 8.45},
    {'nome' : 'Produto 4' , 'preco' : 59.95},
    {'nome' : 'Produto 2' , 'preco' : 109.99},
]

#  progamação com comprehension


def filtrar_preco_maior(p):
    return p['preco'] > 100


# novos_produtos = [
#     {**p, 'preco' : filtrar_preco_maior(p['preco'])}
#     for p in produtos
# ]

#  progamação funcional

novos_produtos = filter(
    # lambda p : p['preco'] > 100, 
    filtrar_preco_maior,
    produtos
)



print_iter(novos_produtos)

'''
Aqui vai mais pelo gosto pois o filter seria a utilização mais funcional do python
porem e possivel realizar a mesma coisa utilizando comprehension

'''