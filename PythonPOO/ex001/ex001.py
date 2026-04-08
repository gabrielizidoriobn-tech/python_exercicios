# declaração de classe
class gafanhoto:
    def __init__(self):# método construtor
        # atributo de instancia
        self.nome = ""
        self.idade = 0

    # metodos de instancia

    def aniversario(self):
        self.idade += 1
    
    def mensagem(self):
        return f'{self.nome} é o gafanhoto(a) e tem {self.idade} anos'

# declaração do objeto
g1 = gafanhoto()
g1.nome = 'gabriel'
g1.idade = 23
g1.aniversario()

print(g1.mensagem())

g2 = gafanhoto()
g2.nome = 'mauro'
g2.idade = 53
g2.aniversario

print(g2.mensagem())

g3 = gafanhoto()
print(g3.mensagem())
