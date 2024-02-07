# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

# aqui temos um classico closure que recebemos uma função
def cria_func(func):
    # guardada a informação da função recebemos agora os valores dos parametros no caso utilizando *args = argumentos não nomeados
    def interna(*args):
        # para cada argumento não nomeados realizamos a restrição vara verificar se o parametro isistance=(param , str)
        for arg in args:
            is_string(arg)
        # no resultado guardamos agora o valor da função passada para a closure e passamos também seu argumento já tratado para dentro da mesma
        resultado = func(*args)
        # retornamos o resultado na def interna(*args)
        return resultado
    # retornamos da dec cria_func(func) o valor da def interna como resultado final da função
    return interna

# a função @cria_func e o sintax sugar utilizando ela não é necessario alterar o codigo na parte de formatar variaveis e trocar
# ordem de puxar as funções pois ao utilizar o sintaxnsugar  estamos automaticamente fazendo com que o invert_string 
# realize a execução primeiramente da cria_func que é onde será tratado os dados antes de gerar a saida
@cria_func
def invert_string(string):
    return string[::-1]

def is_string(arg):
    if not isinstance(arg , str):
        raise TypeError("Deve ser digitado uma string")


user_input = invert_string('123')
print(user_input)



#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


def criadora_de_funcao(func):
    def tratadora_de_param(*args):
        resultado = func(*args)
        return resultado
    return tratadora_de_param

# os decoradores são utilizados de baixo para cima caso necessario atualizar com mais um decorador
@criadora_de_funcao
def soma(x ,y):
    return x + y



somar = soma(2,2)
print(somar)