// Exercício 8: Crie um programa que solicita a idade do usuário e o país de residência. Se a idade for superior a 65 anos ou o país for "Cidade da Aposentadoria", imprima "Você se qualifica para benefícios de aposentadoria"; caso contrário, imprima "Você não se qualifica para benefícios de aposentadoria".

const idade = 12;
const pais = "Cidade da Aposentadoria";

if (idade > 65 || pais === "Cidade da Aposentadoria") {
  console.log("Você se qualifica para benefícios de aposentadoria");
} else {
  console.log("Você não se qualifica para benefícios de aposentadoria");
}
