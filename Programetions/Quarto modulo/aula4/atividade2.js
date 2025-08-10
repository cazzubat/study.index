//Este algoritmo lê uma palavra, usa um laço for...of para iterar sobre cada letra e imprime a letra em caixa alta.

let palavra = 'programação';
for (let letra of palavra) {
  console.log(letra.toUpperCase());
}