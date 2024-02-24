class ContaBancaria:
    def __init__(self, nome , saldoConta):
            self.nome = nome
            self._saldoConta = saldoConta


    def investir(self):
        self._saldoConta
        print(f'Seu saldo em conta é {self._saldoConta}')
        valor = 0
        int(input('Digite o valor que deseja investir: '))
        self.saldoInvestimento = 0

        if valor <= self._saldoConta :
            self.saldoInvestimento = valor
            self._saldoConta - valor

            print (f'\n Voce investiu {valor} e agora seu saldo no investimento e de: {self.saldoInvestimento} \n Seu saldo na sua conta e de {self._saldoConta}')
        
        else:
             print('Você não tem saldo suficiente para investir')
        
        

                

c1 = ContaBancaria('Sergio', 1000)

c1.investir()

