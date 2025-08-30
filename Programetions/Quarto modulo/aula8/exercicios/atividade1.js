// Ex01. Crie um objeto "Carro" que deve conter as propriedades "marca", "modelo", "ano" e "cor"

const Carro = {
    marca: "Toyota",
    modelo: "Corolla",
    ano: 2020,
    cor: "Prata"
};

//a) Mostre no console a marca e o modelo do carro
console.log(Carro.marca, Carro.modelo);

// b) Mostre no console a cor do carro
console.log(Carro.cor);

// b) Mostre no console a cor do carro
console.log(Carro.cor)

// c) Altere o valor da cor do carro (e mostre novamente)
alteracao_cor = Carro["cor"] = "Vermelho"
console.log(Carro.cor)

// d) Adicione uma nova propridade chamada "km" que terá a kilometragem do carro
nova_propriedade = Carro["km"] = 17.5
console.log(Carro.km)