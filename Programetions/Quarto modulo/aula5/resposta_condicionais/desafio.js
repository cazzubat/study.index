const perguntasTexto = [
  "Telefonou para a vítima?",
  "Esteve no local do crime?",
  "Mora próximo do local do crime?",
  "Devia favores/dinheiro à vítima?",
  "Já trabalhou com a vítima?"
];

const respostas = [];

for (let i = 0; i < perguntasTexto.length; i++) {
  const resposta = prompt(perguntasTexto[i]).toLocaleLowerCase();
  if (resposta === "s" || resposta === "sim") { 
    respostas.push(resposta);
}
}

if (respostas.length === 2) {
    console.log("Suspeita");
} else if (respostas.length === 3) {
    console.log("Cúmplice");
} else if (respostas.length >= 4) {
    console.log("Assassino");
} else {
    console.log("Inocente");
}
