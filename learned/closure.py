'''
Closure e funções que retornam outras funções
'''


# def criar_saudacao (saudacao):
#     def saudar(nome):
#         return f'{saudacao}, {nome}'
#     return saudar

# falar_bom_dia = criar_saudacao('bom dia')
# falar_boa_noite = criar_saudacao('boa noite')

# for nome in ['maria' , 'joana' , 'luiz' ,'guilherme']:
#     print(falar_bom_dia(nome))
#     print(falar_boa_noite(nome))

####################################################
    

def multiplicador(multiplicador):
    def multiplica(numero):
        return(f'voce está multiplicando o numero {numero} por {multiplicador}')
    return multiplica

lista_multiplicadores = [ 1, 2, 3, 4, 5]

valor_multiplicar = multiplicador(2)

for n in lista_multiplicadores:
    print(valor_multiplicar(n))

    
print()
print()



