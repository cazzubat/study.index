//Este algoritmo filtra a lista de produtos, verificando se cada item começa ou termina com o caractere 'a' e imprime os resultados.

let produtosDoMercado = ["aveia", "maçã", "uva", "abobora", "leite", "pão", "sabonete", "desodorante", "amaciante", "chuveiro"];
let caractere = 'a';

let produtosFiltrados = produtosDoMercado.filter(produto => 
  produto.startsWith(caractere) || produto.endsWith(caractere)
);

console.log(produtosFiltrados);