# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.


def cria_func(func):
    def interna(*args):
        for arg in args:
            is_string(arg)
        resultado = func(*args)
        return resultado
    return interna
        

def invert_string(string):
    return string[::-1]

def is_string(arg):
    if not isinstance(arg , str):
        raise TypeError("Deve ser digitado uma string")


verifica_se_e_string = cria_func(invert_string)
user_input = verifica_se_e_string(123)
print(user_input)
