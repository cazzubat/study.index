// 7 - Dado o array de numeros abaixo, faça um programa que crie um novo array utilizando o filter, onde ele deve trazer somente os preços maiores que 40 e menores que 100.
const numeros = [12, 45, 76, 34, 65, 87, 88, 12, 344, 200, 445]
const numeros_filtrados = numeros.filter((numeros) => numeros > 40 && numeros < 100)
console.log(numeros_filtrados)