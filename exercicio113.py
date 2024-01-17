
def multiplicaarg(*args):
    args = list(args)
    print(args[0] * args[1])
    i = 0
    x = 0
    y = 1
    acomulador = 0
    while i < len(args):
        multiplicador = args[x] * args[y]
        print(f'x{args[x]} * y{args[y]} = {multiplicador}')
        acomulador += multiplicador
        print(acomulador)
        i+=1
        x+=1
        y+=1
        print(multiplicador)

multiplicaarg(1,2,3,4,5,6)
