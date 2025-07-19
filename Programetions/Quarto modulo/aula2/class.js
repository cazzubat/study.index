class Pessoa{
    constructor(nome, idade) {
        this.nome = nome;
        this.idade = idade;
    }
    
    apresentar() {
        console.log(`Olá, meu nome é ${this.nome} e tenho ${this.idade} anos.`)
    }

    despedir() {
        console.log(`Tchau, até logo.`)
    }
}

const pessoa1 = new Pessoa("Adriano",28)
pessoa1.apresentar();
pessoa1.despedir();