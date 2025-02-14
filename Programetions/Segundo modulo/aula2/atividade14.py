# 7 - Escreva um algoritmo que recebe como entrada um produto, armezena essa informação numa lista e pergunta ao usuário se ele deseja adicionar novos itens à esa lista, quando o usuário não desejar mais adicionar itens, os nomes itens adicionados devem ser impressos no terminal em forma de lista.

lista = []

while True:
    produto = input('Insira um produto para adicionar na lista: ').lower().strip()  # Corrigido o uso de .strip()
    lista.append(produto)  # Adiciona o produto à lista
    print(f'A sua lista foi atualizada: {lista}')
    
    deseja_continuar = input('Deseja continuar? s/n ').lower().strip()  # Verifica se o usuário deseja continuar
    if deseja_continuar != 's':  # Sai do loop se a resposta for diferente de 's'
        break

# Exibe a lista final
print("Os itens da sua lista são: ")
print(lista)
