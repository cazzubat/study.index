// Lista de Participantes
const PARTICIPANTES_KEY = "participantes.sorteio";
const PARTICIPANTES_MAX_ID = "participantes.max-id";

let participantes = localStorage.getItem(PARTICIPANTES_KEY)
  ? JSON.parse(localStorage.getItem(PARTICIPANTES_KEY))
  : [];

let counterId = localStorage.getItem(PARTICIPANTES_MAX_ID)
  ? Number(localStorage.getItem(PARTICIPANTES_MAX_ID))
  : 0;

function generateId() {
  counterId += 1;
  localStorage.setItem(PARTICIPANTES_MAX_ID, counterId.toString());
  return counterId;
}

function LiPartipante(participante) {
  const liParticipante = document.createElement("li"); // <li></li>
  liParticipante.textContent = `${participante.nome} - ${participante.email}`; // <li>${participante}</li>
  liParticipante.classList.add("participante");

  liParticipante.addEventListener("click", () => {
    const confirmacao = confirm(
      `Tem certeza que deseja remover o participante ${participante.nome}?`
    );

    if (!confirmacao) {
      return;
    }

    // Remove o Participante da Lista
    participantes = participantes.filter((p) => p.id != participante.id);
    localStorage.setItem(PARTICIPANTES_KEY, JSON.stringify(participantes));

    // Remove o Elemento HTML do Participante
    liParticipante.remove();
  });

  return liParticipante;
}

// Listar Participantes ao Carregar a Página.
function handleCarregarParticipantes() {
  const ulParticipantes = document.getElementById("participantes");

  for (let participante of participantes) {
    const liParticipante = LiPartipante(participante);
    ulParticipantes.appendChild(liParticipante);
  }
}

window.addEventListener("load", handleCarregarParticipantes);

// Adicionar Participante
function handleAdicionar(event) {
  const form = event.target;

  // Previnir o Comportamento Padrão do Submit (Recarregar a Página)
  event.preventDefault();

  // 1. Buscar o Nome do Participante
  const participante = {
    id: generateId(),
    nome: form.nome.value, // form.<input-id>.value
    email: form.email.value,
  };

  // Validar os dados do participante...

  participantes.push(participante);
  localStorage.setItem(PARTICIPANTES_KEY, JSON.stringify(participantes));

  // 2. Criar o Elemento de Lista com o Participante
  const liParticipante = LiPartipante(participante);

  // 3. Adicionar esse elemento a Lista
  // Busca a lista no HTML.
  const ulParticipantes = document.querySelector("#participantes");

  // Adiciona o elemento na Lista.
  ulParticipantes.appendChild(liParticipante);

  form.reset();
  form.nome.focus();
}

const formParticipante = document.getElementById("participante");
formParticipante.addEventListener("submit", handleAdicionar);

// Sortear
function handleSortear() {
  // Math.random() * (<fim> - <inicio>) + <inicio>
  const indexSorteado = Math.floor(Math.random() * participantes.length);
  const participanteSorteado = participantes[indexSorteado];

  const pResultado = document.querySelector("#resultado");
  pResultado.classList.remove("hidden");

  const spanNome = pResultado.querySelector(".nome");
  spanNome.textContent = participanteSorteado.nome;

  const spanEmail = pResultado.querySelector(".email");
  spanEmail.textContent = participanteSorteado.email;

  // pResultado.innerHTML = `
  //     O participante <span class="highlight">${participanteSorteado.nome}</span> foi sorteado! Entre em contato pelo email: <span class="highlight">${participanteSorteado.email}</span>
  // `
}

const buttonSortear = document.getElementById("sortear");
buttonSortear.addEventListener("click", handleSortear);
