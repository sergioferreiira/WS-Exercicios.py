from functools import partial

def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()


produtos = [
    {'nome' : 'Produto 1' , 'preco' : 12.30},
    {'nome' : 'Produto 5' , 'preco' : 7.00},
    {'nome' : 'Produto 3' , 'preco' : 8.45},
    {'nome' : 'Produto 4' , 'preco' : 59.95},
    {'nome' : 'Produto 2' , 'preco' : 109.99},
]


def aumentar_dez_porcento(produto , porcentagem):
    return round(produto * porcentagem , 2) 

# PARTIAL e como se fosse uma closure
aumentar_preco = partial(
    aumentar_dez_porcento,
    1.1
    )


def mudar_preco(produto):
    return {
        **produto, 
        'preco': aumentar_preco
        (produto['preco']
         )
         }
    

novos_produtos_map = map(
    mudar_preco,
    produtos
)

print_iter(novos_produtos_map)



'''
                    #### MINHA EXPLICAÇÃO ####

    O PARTIAL nada mais é doque uma closure, porém trabalhando com progamação funcional
voce previamente cria uma função que recebe os devidos parametros, o partial vai buscar a função
passando o primeiro valor pois o mesmo está fixado, e voce trabalha passando fixamente o segundo parametro 
no caso acima sendo 1.1, assim reduzindo o codigo.

    MAP o map e mais facil de ser compreendido pois o mesmo e a forma mais curta de mostrar os dados,
em vez de realizar uma dict comprehension fazemos uma nova variavel que utiliza a func MAP() e dentro 
desse MAP passamos o tratamento do dado, já previamente realizado, e o iteravel que ele deve tratar.



'''