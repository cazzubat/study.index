// Exercício 4: Crie um programa que recebe uma string como entrada e verifica se ela começa com a letra 'A'. Imprima "Começa com A" se for verdadeiro, caso contrário, imprima "Não começa com A".

const stringrecebida = "abobora";
const verificar = stringrecebida[0].toLowerCase() === "a"? "Começa com A": "Não começa com A";
console.log(verificar)