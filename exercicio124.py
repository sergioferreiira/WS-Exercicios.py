
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


acerto = 0
erro = 0
indice = 0

for pergunta in perguntas[indice]['Pergunta']:
    print(perguntas[indice]['Pergunta'])
    print("Escolha a alternativa correta")

    contador = 0
    for opcoes in perguntas[indice]['Opções']:
        print(f"{contador}) {opcoes}")
        contador += 1

    opcaolista = perguntas[indice]['Opções'] # tipo list
    conferir_resposta = int(input('Qual alternativa voce escolhe? '))
    
    resposta_correta = int(perguntas[indice]['Resposta']) # tipo int
    
    confirmar_resposta = int(opcaolista[conferir_resposta])
    
    if confirmar_resposta == resposta_correta:
        print("Voce acertou")
        acerto += 1
    else:
        print("Voce errou")
        erro += 1


    indice += 1

    if indice == 3:
        break

print("Essa e a quantidade de acertos = " , acerto)
print("Essa e a quantidade de erros = " , erro)






