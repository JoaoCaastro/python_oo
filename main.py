import carro

uno_vermelho = carro.Carro('Vermelho', 4, 'Flex', 0, 1.0, False, 0)
uno_vermelho.ligar()
uno_vermelho.abastecer(50)
uno_vermelho.abastecer(10)
uno_vermelho.acelerar(50)
uno_vermelho.desligar()

uno_preto = carro.Carro('Preto', 2, 'Gasolina', 0, 1.4, False, 0)
uno_preto.ligar()
uno_preto.abastecer(10)
uno_preto.desligar()
