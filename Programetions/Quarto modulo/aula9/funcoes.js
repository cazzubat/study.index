// Funções (Revisão)
// Uma função é uma ação onde nós definimos entrada, processamento e saída

// Assinatura da Função
// function <nomeFunção>(<parametros>...) {
//      <codigo da funcao>
// }

/**
 * Mostra uma saudação no console para uma pessoa
 * @param {string} nome - Nome da pessoa
 * @param {string} sobrenome - Sobrenome da pessoa (Opcional)
 * @returns {void}
 */
function mostrarSaudacao(nome, sobrenome = "") {
  console.log(`Olá ${nome} ${sobrenome}`);
}

mostrarSaudacao("Alessandra");
mostrarSaudacao("Usuário", "Infinity");

// Retornos de Função

// Ao retornar um valor em uma função, esse valor vai substituir o local da chamada da função.
function calcularImc(peso, altura) {
  const imc = peso / (altura * altura);
  return imc;
}

// Armazenando o retorno da função em uma variavel
const variavel = calcularImc(75, 1.71);
console.log(variavel);

// Passando o retorno da função como parametro para outra função
console.log(calcularImc(85, 1.67));
