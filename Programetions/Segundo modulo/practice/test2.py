
print("Cadastro de produtos e cálculo do valor total da compra")

produtos = {}
valor_total = 0  

for vezes in range(5):
    nome = input(f"Digite o nome do produto {vezes + 1}: ")
    preco = float(input(f"Digite o preço de '{nome}': R$ "))
    produtos[nome] = preco 
    valor_total += preco   


print("\nProdutos cadastrados:")
for produto in produtos: 
    print(f"{produto}: R$ {produtos[produto]:.2f}") 

print(f"\nValor total da compra: R$ {valor_total:.2f}")