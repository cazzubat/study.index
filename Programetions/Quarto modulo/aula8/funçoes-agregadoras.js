// Map
const numeros = [1, 2, 3, 4, 5];
const numerosMultiplicados = numeros.map((numero) => numero * 2);
console.log(numerosMultiplicados); // [2, 4, 6, 8, 10]

// Filter
const numerosPares = numeros.filter((numero) => numero % 2 === 0);
console.log(numerosPares); // [2, 4]

// Reduce
const soma = numeros.reduce((acumulador, numero) => acumulador + numero, 0);
console.log(soma); // 15

// Find
const primeiroNumeroPar = numeros.find((numero) => numero % 2 === 0);
console.log(primeiroNumeroPar); // 2

// Some
const temNumeroMaiorQueTres = numeros.some((numero) => numero > 3);
console.log(temNumeroMaiorQueTres); // true

// Every
const todosSaoMenoresQueDez = numeros.every((numero) => numero < 10);
console.log(todosSaoMenoresQueDez); // true

// ForEach
const nomes = ['Ana', 'Ju', 'Leo', 'Paula', 'Marcos'];
nomes.forEach((nome) => console.log(nome.toUpperCase()));