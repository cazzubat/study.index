//Este algoritmo usa um laço for para combinar os nomes e sobrenomes das duas listas e imprimir o nome completo.

let nomes = ['Bruna', 'Gabriel', 'Marcos', 'Jéssica', 'Fernando'];
let sobrenomes = ['Oliveira', 'Santos', 'Marques', 'Castro', 'Silva'];

for (let i = 0; i < nomes.length; i++) {
  console.log(`${nomes[i]} ${sobrenomes[i]}`);
}