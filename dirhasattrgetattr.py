string = "luiz"
metodo = 'upper'

if hasattr(string, metodo):
    print("existe upper")
    print(getattr(string, metodo)())