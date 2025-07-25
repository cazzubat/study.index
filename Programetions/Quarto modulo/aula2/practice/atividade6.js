// Exercício 6: Crie um programa que determina se um ano dado é bissexto. Um ano bissexto é divisível por 4, mas não é divisível por 100, a menos que também seja divisível por 400.

const ano = 2025;
verificar = (ano % 4 === 0) && (ano % 100 !== 0)? "Ano bissexto": "Não é ano bissexto";
console.log(verificar)