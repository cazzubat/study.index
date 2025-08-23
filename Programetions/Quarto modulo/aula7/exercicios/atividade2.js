// 2 - Faça um programa onde você declare um array com 6 precos, depois utilize a função "map" para criar um novo array de precos onde deve ser aplicado um desconto de 20% em todos eles.
const precos = [40.9, 44.99, 20, 10, 12.3, 15]
const desconto = precos.map((preco) => (preco * 0.8).toFixed(2))
console.log(desconto)