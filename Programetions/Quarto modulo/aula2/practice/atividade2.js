// Exercício 2: Crie um programa que verifica se um número dado é par ou ímpar e imprime o resultado.

const numerodado = 10;
const verificar = (numerodado % 2) === 0? "Par": "Impar";
console.log(`Esse numéro é: ${verificar}`)