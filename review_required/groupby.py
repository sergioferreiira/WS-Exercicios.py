# from itertools import groupby 

# alunos = [
#     {'nome': 'Luiz', 'nota': 'A'},
#     {'nome': 'Letícia', 'nota': 'B'},
#     {'nome': 'Fabrício', 'nota': 'A'},
#     {'nome': 'Rosemary', 'nota': 'C'},
#     {'nome': 'Joana', 'nota': 'D'},
#     {'nome': 'João', 'nota': 'A'},
#     {'nome': 'Eduardo', 'nota': 'B'},
#     {'nome': 'André', 'nota': 'A'},
#     {'nome': 'Anderson', 'nota': 'C'},
# ]



# alunos_ordenados = sorted(alunos, key= lambda aluno: aluno['nota'])
# grupo_de_notas = groupby(alunos_ordenados, key= lambda aluno: aluno['nota'])


# for grupo , nota in grupo_de_notas:
#     print(grupo)
#     for nota in nota:
#         print(nota)


#  EXERCICIOS

from itertools import groupby

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def par_impar(numero):
    return 'par' if numero % 2 == 0 else 'impar' 

numeros_organizados = sorted(numeros , key= par_impar)
print(numeros_organizados)
resultado = groupby(numeros_organizados , key= par_impar)

for grupo , numeros in resultado:
    print(grupo)
    print([*numeros])