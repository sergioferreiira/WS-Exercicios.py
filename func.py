def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)


#  CALL STACKS
#  E como funciona as funçoes e seus escopos EX:

x = 1

def funcao():
    x = 10
    print(x)
    def outra_funcao():
        x = 11
        y = 12
        print(x , y)
        
    outra_funcao()
    print(x)

print(x)
funcao()
print(x)