class Veiculo:
    def __init__(self, cor, preco):
        self.cor = cor
        self.preco = preco
    
    def detalhes(self):
        return f"Cor: {self.cor}\nPreço: R${self.preco:.2f}"


class Carro(Veiculo):
    def __init__(self, cor, preco, numero_portas):
        super().__init__(cor, preco)
        self.numero_portas = numero_portas
    
    def detalhes(self):
        base_details = super().detalhes()
        return f"{base_details}\nNúmero de portas: {self.numero_portas}"


class Bicicleta(Veiculo):
    def __init__(self, cor, preco, tipo):
        super().__init__(cor, preco)
        self.tipo = tipo
    
    def detalhes(self):
        base_details = super().detalhes()
        return f"{base_details}\nTipo: {self.tipo} bike"

carro = Carro(cor="Azul", preco=30000, numero_portas=4)
bicicleta = Bicicleta(cor="Vermelha", preco=1500, tipo="Montanha")

print("Detalhes do Carro:")
print(carro.detalhes())
print("\nDetalhes da Bicicleta:")
print(bicicleta.detalhes())
