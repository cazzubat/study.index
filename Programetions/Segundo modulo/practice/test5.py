class Veiculo:
    def movimentar(self):
        print("Veículo está em movimento.")

class Carro(Veiculo):
    def movimentar(self):
        print("Carro está dirigindo.")

class Moto(Veiculo):
    def movimentar(self):
        print("Moto está acelerando.")

# Exemplo de uso
def main():
    veiculo = Veiculo()
    carro = Carro()
    moto = Moto()
    
    veiculo.movimentar()
    carro.movimentar()
    moto.movimentar()

if __name__ == "__main__":
    main()
