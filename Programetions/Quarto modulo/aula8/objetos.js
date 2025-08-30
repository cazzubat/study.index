const pessoas = [
    { nome: "Ana", idade: 25 },
    { nome: "Bruno", idade: 30 },
    { nome: "Carla", idade: 28 }
];

const somaIdades = pessoas.reduce((acumulador, pessoa) => acumulador + pessoa.idade, 0);

console.log(`A soma das idades é: ${somaIdades}`);

const mediaIdades = somaIdades / pessoas.length;

console.log(`A média das idades é: ${mediaIdades.toFixed(2)}`);