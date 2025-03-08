class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self._saldo = saldo_inicial 

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque deve ser positivo.")
        elif valor > self._saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def exibir_saldo(self):
        print(f"Saldo atual da conta de {self._titular}: R$ {self._saldo:.2f}")

# Exemplo de uso
conta = ContaBancaria("João da Silva", 1000)
conta.exibir_saldo()
conta.depositar(500)
conta.sacar(200)
conta.exibir_saldo()
conta.sacar(2000)
