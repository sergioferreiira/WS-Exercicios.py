
'''
conhecimento de funções recursivas para utilização no python caso queira
porém não passa de um loop, a depender da linguagem temos utilização pura
'''


def factorial(n):
    if n <= 1:
        return n
    
    return n * factorial(n - 1)
