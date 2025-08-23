// 8 - Dado o array de nomes, você deve filtrar (filter) todos os nomes que contém "joão" (ignore se é maiusculo ou minusculo), e depois crie um novo array onde todos os nomes devem estar em maiúsculo (map).
const nomes = [
    "Davi",
    "Guilherme",
    "João Pedro",
    "João Guilherme",
    "Maria",
    "Carlos JOÃO",
    "joão",
    "jOÃo Victor",
    "Victor",
    "Fernanda",
    "Lara",
    "Thays"
]

const nomes_filtrados = nomes.filter((nome) => nome.toLowerCase().includes("joão"))
console.log(nomes_filtrados)

const nomes_maiusculo = nomes.map((nome) => nome.toUpperCase())
console.log(nomes_maiusculo)