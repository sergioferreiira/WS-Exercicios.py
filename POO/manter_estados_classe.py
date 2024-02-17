
class Camera:
    def __init__(self, nome , filmando = False):
        self.nome = nome
        self.filmando = filmando

    def iniciar_filmagem(self):
        self.filmando = True
        print(f"A gravação da {self.nome} começou...")
        

    def parar_filmagem(self):
        print(f"A gravação da {self.nome} parou")
        self.filmando = False
        
    
    def fotografar(self):
        if self.filmando is True:
            print(f'Não e possivel fotografar com a {self.nome} enquanto ela está gravando.')
            return
        print(f'A camera {self.nome} está fotografando')


c1 = Camera('Tec Pix')



c1.iniciar_filmagem()
c1.parar_filmagem()
c1.fotografar()
