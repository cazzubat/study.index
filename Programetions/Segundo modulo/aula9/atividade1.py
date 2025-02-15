class Livro:
    def __init__(self, titulo, autor, ano, categoria, editora, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.categoria = categoria
        self.editora = editora
        self.ISBN = ISBN
        
    def __str__(self):
        return f'{self.titulo} | {self.autor} | {self.ano} | {self.categoria} | {self.editora} | {self.ISBN} '

class Estante:
    def __init__(self, didaticos, literatura, cronica, romcance, terror):
        self.ditaticos = didaticos
        self.literaturas = literatura
        self.cronica = cronica
        self.romance = romcance
        self.terror = terror

class Usuario:
    def __init__(self, nome, cpf, numero_de_matricula):
        self.nome = nome
        self.cpf = cpf
        self.numero_de_matricula = numero_de_matricula

class Funcionario:
    def __init__(self, id, nome_funcionario, senha):
        self.nome_funcionario = nome_funcionario
        self.id = id
        self.senha = senha
        

class Biblioteca:
    def __init__(self, endereço, nome_biblioteca, telefone):
        self.endereço = endereço
        self.nome_biblioteca = nome_biblioteca
        self.telefone = telefone

memorias = Livro('Memórias póstumas', 'Machadão', '1898', 'romance', 'primeiro de abril', '01A')
print(memorias)
