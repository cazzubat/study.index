// 3 - Faça um programa onde você declare um array com 5 nomes, depois utilize a função "map" para criar um novo array onde todos os nomes devem estar em maiúsculo (.toUpperCase).
const nomes = ["Ana", "Carlos", "Beatriz", "Lucas", "Mariana"];
const nomes_maiusculo = nomes.map((nomes) => nomes.toUpperCase())
console.log(nomes_maiusculo)