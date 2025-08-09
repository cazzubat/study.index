const genero = String(prompt("Digite seu genero:"))
const altura = parseFloat(prompt("Digite sua altura: "))
const peso = parseFloat(prompt("Digite seu peso: "))

const imc = peso / (altura * altura)

let classificacao = "";

if (imc < 18.5) {
    classificacao = "Abaixo do peso";
    } else if (imc < 25) {
    classificacao = "Peso normal";
    } else if (imc < 30) {
    classificacao = "Sobrepeso";
    } else if (imc < 35) {
    classificacao = "Obesidade grau 1";
    } else if (imc < 40) {
    classificacao = "Obesidade grau 2";
    } else {
    classificacao = "Obesidade grau 3 (mórbida)";
}

alert(`Seu IMC é ${imc}, você está classficado como ${classificacao}.`)