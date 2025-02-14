# 5 - Um supermercado está precisando de um sistema capaz de listar todos os produtos a partir de uma busca simples, o usuário deve ser capaz de procurar um produto pelo nome, parcial ou completo. Segue uma lista de exemplo:
produtos = [
    "Camiseta", "Calça jeans", "Tênis", "Mochila", "Notebook", "Fones de ouvido",
    "Smartphone", "Relógio", "Óculos de sol", "Garrafa de água", "Câmera", 
    "Console de jogos", "Livros", "Mesa", "Cadeira", "Luminária de mesa", 
    "Caderno", "Estojo", "Marcadores", "Pincéis de pintura", "Tela de pintura", 
    "Violão", "Teclado", "Microfone", "Drone", "Barraca de camping", "Saco de dormir", 
    "Botas de caminhada", "Bússola", "Lanterna", "Bicicleta", "Capacete", "Skate", 
    "Patins", "Bola de basquete", "Bola de futebol", "Taco de beisebol", 
    "Tacos de golfe", "Vara de pescar", "Raquete de tênis", "Roupa de banho", 
    "Protetor solar", "Toalha de praia", "Cesta de piquenique", "Churrasqueira", 
    "Cooler", "Jogos de tabuleiro", "Relógio de parede", "Ferro de passar roupa", 
    "Aspirador de pó", "Vaso de flores", "Chaleira", "Panela de pressão"
]

escolha = input('Insira uma letra para filtrar os produtos: ').lower()

resultado = []

for produto in produtos:
    if escolha in produto.lower():  
        resultado.append(produto)  


if resultado:
    print(f"Produtos que contêm a letra '{escolha}':")
    for item in resultado:
        print(item)
else:
    print("Nenhum produto encontrado.")