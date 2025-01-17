# 9 - Crie um algoritmo para que o usuário possa selecionar uma das três opções: "pedra", "papel", "tesoura"
# imprima a opção escolhida pelo usuário.

print('Escolha uma dentre essas opções: Pedra, Papel ou Tesoura.')

opções = ["pedra", "papel", "tesoura"]

escolha = input("Qual é a sua escolha? ").lower().strip()

if escolha in opções:
    print(f"Você escolheu {escolha}") 

while escolha not in opções:
    print("Escolha inválida. Por favor, escolha uma das opções")
    
    escolha = input("Qual é a sua escolha? ")
    print(f"Você escolheu {escolha}") 