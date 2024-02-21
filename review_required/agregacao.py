# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).



class CarrinhoDeCompras:
    def __init__(self):
        self._produtos = []

    def inserirProdutos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)
    
    def somarCarrinho(self):
        return sum([p.preco for p in self._produtos])
    
    def listarCarrinho(self, total):
        for produto in self._produtos:
            print(produto.nome , produto.preco)
        print()
        print(f'A soma total dos produtos é : R${total:.2f}')

class Produto:
    def __init__(self, nome , preco):
        self.nome = nome
        self.preco = preco

carrinho = CarrinhoDeCompras()
p1 , p2 , p3 = Produto('camisa' , 21), Produto('calça' , 37), Produto('tenis' , 189)

carrinho.inserirProdutos(p1,p2,p3)

total = carrinho.somarCarrinho()

print(carrinho.listarCarrinho(total))


