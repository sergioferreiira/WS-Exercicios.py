from itertools import product



user_input1 = input("digite o valor a: ")
user_input2 =  input("digite o valor b: ")

def recebedor_de_lista(*lista1):
    def unidor_de_lista(*lista2):
        resultado = list(product(lista1 , lista2))
        return resultado
    return unidor_de_lista



unindo = recebedor_de_lista(user_input1)
uniu = unindo(user_input2)

print(uniu)