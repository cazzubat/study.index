# Importando bibliotecas
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Dados de exemplo (frases de clientes)
comentarios = ["A entrega foi muito rápida, estou satisfeito!",
               "O atendimento foi péssimo, não recomendo!",
               "Produto de ótima qualidade, voltarei a comprar.",
               "Demorou muito para chegar, experiência ruim."]

# Rótulos das frases (positivo ou negativo)
sentimentos = ["positivo", "negativo", "positivo", "negativo"]

# Convertendo texto para números
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(comentarios)

# Criando e treinando o modelo
modelo = MultinomialNB()
modelo.fit(X, sentimentos)

# Testando com um novo comentário
novo_comentario = []
for i in range(2): 
    novo_comentario.append(input('Insira uma frase para testar: '))
X_novo = vectorizer.transform(novo_comentario)
previsao = modelo.predict(X_novo)

print(f"O sentimento do comentário é: {previsao[0]}")
