const numeroUsuario = parseInt(prompt("Digite um número:"));
let soma = 0;
let i = 1;

while (i <= numeroUsuario) {
  soma += i;
  i++;
}

console.log(soma);