# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    print('linha 1')
    c = a / b
    print('linha 2')
except ZeroDivisionError:
    print('dividiu por zero')
