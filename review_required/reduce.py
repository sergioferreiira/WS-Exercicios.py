from functools import reduce


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


total = reduce(
    lambda ac , p : ac + p['preco'],
    produtos,
    0
)

print(total)