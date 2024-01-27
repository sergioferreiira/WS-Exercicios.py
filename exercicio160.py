import copy

from importar_package import produtos


# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)


# novos_produtos = [
#     {**p, 'preco': round(p['preco'] * 1.1 , 2)}
#     for p in copy.deepcopy(produtos)

# ]

# print(*produtos, sep="\n")
# print()
# print(*novos_produtos, sep="\n")
# print()


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# produtos_ordenados_por_nome = sorted(
#     produtos,
#     key=lambda p: p['nome']
# )

# print(*produtos_ordenados_por_nome, sep="\n")
# print()


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

# produtos_ordenados_por_nome = sorted(
#     produtos,
#     key=lambda p: p['nome'],
#     reverse=True
# )
# print()
# print(*produtos_ordenados_por_nome, sep="\n")
# print()


# import copy

# from importar_package import produtos

# print(*produtos, sep="\n")


# def mostro_kwargs(*args , **kwargs):
#     print(args)
    
#     print(*kwargs.values() , sep="\n")

# mostro_kwargs(1 ,2, 3,
#     nome= 'Produto 5', preco= 10.00,
#     nome2= 'Produto 1', preco2= 22.32,)