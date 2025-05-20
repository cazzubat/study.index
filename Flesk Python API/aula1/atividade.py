import requests


print('Busca INFO de Países')
while True:
    print('Informe o nome do páis ou <Enter> para sair')
    opcao = input()
    if not opcao:
        break
    # params = {'usuario': 'murilo', 'id': 123}
    try:
        url = f'https://restcountries.com/v3.1/translation/{opcao}' #endpoint
        response = requests.get(url)
        print(f"URL requisitada: {response.url}")
        print(f"Status Code: {response.status_code}")
        dados = response.json()
        #print("Resposta JSON:", response.json())
        print(dados[0]['name']['official'])
        print(dados[0]['flags']['svg'])
    except requests.RequestException as e:
        print("Erro na requisição GET:", e)