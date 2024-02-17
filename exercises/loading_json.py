import json


with open('salvando_exercicio.json', 'r' , encoding='utf-8') as arquivo:
    mouse = json.load(arquivo)
    print(mouse)