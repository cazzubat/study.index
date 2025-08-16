// 5 - Crie um programa que filtra a lista produtos pela letra "e"


const produtos = [
    "Café",
    "Arroz",
    "Feijão",
    "Azeite de Oliva",
    "Pão",
    "Leite",
    "Queijo",
    "Manteiga",
    "Macarrão",
    "Chocolate"
];

const listar = () => {
    for (const item of produtos)
        if (item.toLocaleLowerCase().includes("e")) {
            console.log(`${item} Contém a letra 'e'.`);
}}

listar()