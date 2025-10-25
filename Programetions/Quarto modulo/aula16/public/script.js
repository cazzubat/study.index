const API_URL = "http://localhost:8080";

function criarLinhaProduto(produto) {
  const trProduto = document.createElement("tr");

  const tdNome = document.createElement("td");
  tdNome.textContent = produto.nome;
  trProduto.appendChild(tdNome);

  const tdCategoria = document.createElement("td");
  tdCategoria.textContent = produto.categoria;
  trProduto.appendChild(tdCategoria);

  const tdPreco = document.createElement("td");
  tdPreco.textContent = produto.preco.toLocaleString("pt-BR", {
    style: "currency",
    currency: "BRL",
  });
  trProduto.appendChild(tdPreco);

  return trProduto;
}

async function handleCarregarProdutos() {
  const response = await fetch(`${API_URL}/produtos`);
  const data = await response.json();

  const tableData = document.querySelector("#produtos-table tbody");

  for (let produto of data) {
    const trProduto = criarLinhaProduto(produto);
    tableData.appendChild(trProduto);
  }
}

window.addEventListener("load", handleCarregarProdutos);

async function handleCadastrarProduto(event) {
  event.preventDefault();

  const form = event.target;

  const produto = {
    nome: form.nome.value,
    categoria: form.categoria.value,
    preco: Number(form.preco.value),
  };

  const response = await fetch(`${API_URL}/produtos`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(produto),
  });

  if (!response.ok) {
    alert("Error ao cadastrar produto.");
    return;
  }

  const tableData = document.querySelector("#produtos-table tbody");

  const trProduto = criarLinhaProduto(produto);
  tableData.appendChild(trProduto);

  form.reset();
}

const formProduto = document.getElementById("produtos-form");
formProduto.addEventListener("submit", handleCadastrarProduto);
