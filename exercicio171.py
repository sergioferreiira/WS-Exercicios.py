lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]


new_list = [
    x + y for x , y in zip(lista_a,lista_b)
]

print(new_list)
# def somar_listas(l1 , l2):
#     menor_valor_entre_listas = min(len(l1), len(l2))
#     new_list= [l1[i] + l2[i] for i in range(menor_valor_entre_listas)]
#     return new_list

# print(somar_listas(lista_a, lista_b))


# def somar_listas(l1,l2):
#     if l1 > l2:
#         x = 0
#         new_list=[]
#         while x < len(l2):
#             conta = l2[x] + l1[x]
#             new_list.append(conta)
#             x +=1
#     else:
#         x = 0
#         new_list=[]
#         while x < len(l1):
#             conta = l1[x] + l2[x]
#             new_list.append(conta)
#             x +=1
#     print(new_list)

# somar_listas(lista_b, lista_a)


# new_soma = []

# for n in range(len(lista_b)):
#     new_soma.append(lista_a[n] + lista_b[n])

# print(new_soma)