# class Conta:
#     def __init__(self, numero, titular):
#         self.numero = numero
#         self.titular = titular
#         self.saldo = 0

# if __name__ == "__main__":
#     c1 = Conta(1, 'rafael')



def eh_palindromo(texto):
    for i in range(len(texto)):
        if texto[i] != texto[-1-i]:
            return False
    return True

entrada = ['arara', 'elefante', 'radar' , 'banana']
palindromo = []


for palavra in entrada:
    if(eh_palindromo(palavra)):
        palindromo.append(palavra)

print(palindromo)