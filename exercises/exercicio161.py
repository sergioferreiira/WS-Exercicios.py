# Exercício - Adiando execução de funções

def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


#  logo na assinatura da função armazenamos os dados da funcao que será utlizada 
# e seu primeiro parametro pois queremos manipular apenas o segundo
def executa_funcao_primeiro_parametro(funcao, x):
    # nesta assinatura e quando o usuario ira interagir e passar o parametro que pode ser alterado
    def segundo_parametro(y):
        # aqui temos a utilização dos dois primeiros parametros que estavam guardados na memoria
        return funcao( x , y )
    return segundo_parametro

# passamos para deentro de duas variaveis com nome mais facil e já definimos o seu valor padrao
#  no caso o valor do primeiro parametro
soma_com_cinco = executa_funcao_primeiro_parametro(soma, 5)
multiplica_por_dez = executa_funcao_primeiro_parametro(multiplica, 10)

print(soma_com_cinco(15))
print(multiplica_por_dez(15))



# E aqui temos um classico closure