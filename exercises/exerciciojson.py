import json


class Mouse:
    def __init__(self, marca , nome , botoes):
        self.marca = marca
        self.nome = nome
        self.botoes = botoes



corsair = Mouse('corsair', 'gpro', 17)

caminho_arquivo = 'C:\\Users\\Sergio Ferreira\\Desktop\\ws-python\\exercises\\'
caminho_arquivo += 'salvando_exercicio.json'

salvar = vars(corsair)

with open('salvando_exercicio.json', 'w' , encoding='utf-8') as arquivo:
    json.dump(salvar , arquivo , indent= 2)