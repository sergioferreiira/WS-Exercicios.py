# uma lista com 3 comandos 1 - listar 2 - desfazer 3 - refazer
import os
import json


tarefas = []
tarefas_refazer = []

def salvar ():
    with open('tarefas.json', 'w' ) as arquivo:
        json.dump(tarefas, arquivo, indent=2 , ensure_ascii=False)

while True:

    
    print('Comandos: listar, desfazer , refazer')
    user_input = input('Digite uma tarefa ou comando ')
    print()


    if user_input == "desfazer":
        if len(tarefas) > 0:
            tarefas_refazer.append(tarefas[-1])
            del tarefas[-1]
        else:
            continue
        print()

    elif user_input == "refazer":
        if len(tarefas_refazer) > 0:
            tarefas.append(tarefas_refazer[-1])
            del tarefas_refazer[-1]
        else:
            continue
        print()
    elif user_input == "listar":
        print(tarefas)
        print()

    elif user_input == "salvar":
        salvar()
        print()

    elif user_input == "clear":
        os.system('cls')

    else:
        tarefas.append(user_input)


