import json

pessoa = {
    'nome': 'Luiz Otávio ',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

novo_arquivo_caminho = 'C:\\Users\\Sergio Ferreira\\Desktop\\ws-python\\review_required\\'
novo_arquivo_caminho += 'auladoluiz.json'

'''
ensure_ascii=False e para fazer com que o item salvo no json fique formatado sem os problemas ascii
'''

'''
    Aqui temos como criar um arquivo em json \/
'''
with open(novo_arquivo_caminho , 'w+') as arquivo:
    json.dump(pessoa, arquivo , ensure_ascii=False , indent= 2 )
'''
    Aqui temos como abrir ou buscar atributos \/
'''
with open(novo_arquivo_caminho , 'r') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['nome'])



'''
 CASO QUEIRA PROCURAR UM ARQUIVO OU ABRIR O MESMO EM UMA PASTA OU LUGAR DIFERENTE BASTA CRIAR UMA VARIAVEL
 COM A LOCALIZAÇÃO DO MESMO 
'''
# caminho_arquivo = 'C:\\Users\\Sergio Ferreira\\Desktop\\teste\\'
# caminho_arquivo += 'texto_teste.txt'


# arquivo = open(caminho_arquivo, 'w')
# print('ola mundo')
# arquivo.close
'''
A utilização do (A) exclui o arquivo antigo e reescreve o nosso item passado
'''
# with open(caminho_arquivo, 'w') as arquivo:
#     arquivo.write('linha 1\n')

'''
APPEND MODE muito util em arquivos de log utilizando o (A) pois o mesmo não exclui os arquivos salvos como o (W)
assim salvando e podendo recuperar os arquivos antigos caso necessario

EX:
'''

# with open(caminho_arquivo, 'a') as arquivo:
#     arquivo.write('esse e um append \n')

'''
enconding utf 8 e para que o windowns não de erro em gravar os dados passados para o arquivo.txt
'''

# with open(caminho_arquivo, 'a' , encoding='utf-8') as arquivo:
#     arquivo.write('esse e outro appendão')