// 4 - Faça um programa que tenha um array com 10 numeros (negativos e positivos), utilize o filter para criar um array somente com os numeros positivos.

const numeros = [-5, -3, 0, 2, 8, -1];
const numeros_filtrados = numeros.filter((numeros) => numeros >= 0)
console.log(numeros_filtrados)