# Variáveis livres + nonlocal (locals, globals)

def fora(x):
    # (a) neste caso e considerado uma variavel local da função fora
    a = x
    def dentro():
        # na função dentro é possivel acessar o valor de a porém o mesmo ainda e da função fora
        # caso eu tente utilizar o mesmo dentro da função (dentro) o python entenderia como se
        # eu estivesse criando uma nova variavel e não utilizando (a) que está na função (fora)
        return a
    return dentro


dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())


############## EXEMPLO ##############

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        # aqui foi necessario pois o python entendeu como dito acima, achou que seria uma nova criação de variavel
        # e entao e necessario utilizar como se fosse global() , porém para funções closure utiliza nonlocal
        nonlocal valor_final
        valor_final += valor_a_concatenar

        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)