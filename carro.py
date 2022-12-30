class Carro():

    '''Classe carro, Classe criada para criação de outros objetos do tipo carro'''
    def __init__(self, cor, qtd_portas, tipo_combustivel, qtd_combustivel, potencia, is_ligado, velocidade):
        self.cor = cor
        self.qtd_portas = qtd_portas
        self.tipo_combustivel = tipo_combustivel
        self.qtd_combustivel = qtd_combustivel
        self.potencia = potencia
        self.is_ligado = is_ligado
        self.velocidade = velocidade

    def abastecer(self, qtd_combustivel):
        '''Método que incrementa a quantidade de combustível na variável qtd_combustivel'''
        self.qtd_combustivel += qtd_combustivel
        print(f'O carro possui: {self.qtd_combustivel}L de combustível')

    def ligar(self):
        if self.is_ligado:
            print("O carro está ligado")
        else:
            self.is_ligado = True
            print("Ligando o carro")

    def desligar(self):
        if self.is_ligado == False:
            print("O carro já está desligado")
        else:
            self.is_ligado = False
            print("Desligando o carro")

    def acelerar(self, velocidade=10):
        if self.is_ligado:
            self.velocidade += velocidade
            print(f"Você acelerou a {self.velocidade}KM/H")
        else:
            print("O carro precisa estar ligado para acelerar")