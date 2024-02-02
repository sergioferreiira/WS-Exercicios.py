from itertools import groupby 

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]



alunos_ordenados = sorted(alunos, key= lambda aluno: aluno['nota'])
grupo_de_notas = groupby(alunos_ordenados, key= lambda aluno: aluno['nota'])


for grupo , nota in grupo_de_notas:
    print(grupo)
    for nota in nota:
        print(nota)