# 4b - Uma empresa de automóveis está criando um sistema para cadastrar novos veículos, crie um algoritmo capaz de registrar novos veículos a partir de entradas fornecidas pelo usuário. As informações necessárias são: Modelo, ano, descrição, valor de entrada, valor de parcela e valor total. O valor de entrada é sempre 12% do valor total do veículo e o número máximo de parcelas é sempra té 18 parcelas do valor restante.

informacoes = {}


informacoes['modelo'] = input('Insira o modelo do carro: ')
informacoes['ano'] = input('Insira o ano do carro: ')
informacoes['descricao'] = input('Insira a descrição do carro: ')
informacoes['valor_entrada'] = input('Insira o valor de entrada: ')
informacoes['valor_final'] = input('Insira o valor total: ')

print("\nInformações do veiculo:")
print(informacoes)