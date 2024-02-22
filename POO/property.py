
'''
NESTE CODIGO ABAIXO APRESENTAMOS UM MEIO DE UTILIZAR UM ATRIBUDO SEM DAR ERRO NO CLIENTE,
EM VEZ DE ALTERAR O NOME COR_TINTA EM TODOS OS CLIENTES PODE APENAS CRIAR UMA FUNÇÃO QUE RETORNA O ATRIBUTO
COR_TINTA PARA O CLIENTE, ASSIM PODENDO ALTERAR O CODIGO DO ATRIBUDO SEM DAR ERRO COM O CLIENTE
'''

# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         return self.cor_tinta


# c1 = Caneta('azul')

# print(c1.get_cor())


'''
    JA NESSE CODIGO ABAIXO UTILIZANDO @PROPERTY ESTAMOS AQUI UTILIZANDO DE UMA FUNÇÃO PARA VIRAR UM ATRIBUTO
    OU SEJA A FUNÇÃO COR NÃO SERÁ UTILIZADA COMO FUNÇÃO E SIM COMO ATRIBUTO, CASO SEJA PASSADO () VAI DAR ERRO
    POIS O PROPERTY TRANSFORMA EM ATRIBUTO DE CLASSE
'''

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta


c1 = Caneta('azul')

print(c1.cor)
