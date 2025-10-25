import cors from "cors";
import express from "express";

import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);


let idCount = 0;

function criarId() {
  idCount += 1;
  return idCount;
}

const produtos = [];

const app = express();

app.use(cors());
app.use(express.json());
app.use(express.static("public"));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

app.get("/produtos", (req, res) => {
  res.json(produtos);
});

app.post("/produtos", (req, res) => {
  const data = req.body;

  if (!data.nome) {
    return res.status(400).json({ message: "O campo 'nome' é obrigatório." });
  }

  if (!data.categoria) {
    return res
      .status(400)
      .json({ message: "O campo 'categoria' é obrigatório." });
  }

  if (!data.preco) {
    return res.status(400).json({ message: "O campo 'preco' é obrigatório." });
  }

  const produto = {
    id: criarId(),
    nome: data.nome,
    categoria: data.categoria,
    preco: Number(data.preco),
  };

  if (isNaN(produto.preco)) {
    return res
      .status(400)
      .json({ message: "O campo 'preco' deve ser um numero." });
  }

  produtos.push(produto);
  res.json({ message: "Produto cadastrado com sucesso." });
});

app.get("/produtos/:id", (req, res) => {
  const { id } = req.params;
  const produto = produtos.find((p) => p.id == id);

  if (!produto) {
    res.json({ message: "Produto não encontrado" });
    return;
  }

  res.json(produto);
});

app.listen(8080, () =>
  console.log("Server is running at http://localhost:8080/")
);