// Exercício 10: Crie um programa que solicita ao usuário 4 notas, e calcula a média dessas notas, caso a nota seja superior a 7, o programa deve mostrar na tela a mensagem: "Parabens você foi aprovado", caso contrário, imprima a mensagem: "Infelizmente você não foi aprovado, prepare-se para a recuperação final".

const notas = [8.5, 7.0, 6.5, 9.0];

const soma = notas.reduce((acc, val) => acc + val, 0);
const media = soma / notas.length;

if (media > 7) {
  console.log("Parabéns você foi aprovado");
} else {
  console.log("Infelizmente você não foi aprovado, prepare-se para a recuperação final");
}
