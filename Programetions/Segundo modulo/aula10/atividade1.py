class Livro:
    def __init__(self, titulo, autor, ano, categoria, editora, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.categoria = categoria
        self.editora = editora
        self.ISBN = ISBN
        self.emprestado = False

    def __str__(self):
        return self.titulo


class Pessoa:
    def __init__(self, nome, sobrenome, matricula, endereco, cpf, data_de_nascimento, funcao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.matricula = matricula
        self.endereco = endereco
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento
        self.status = True
        self.funcao = funcao

class Biblioteca:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.catalogo = []
        self.usuarios = []
        self.funcionarios = []

    def cadastrar_usuarios(self, usuario: Pessoa):
        self.usuarios.append(usuario)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)
    
    def cadastrar_livros(self, livro:Livro):
        self.catalogo.append(livro)
        print('Livro cadastrado com sucesso!')

    def emprestar_livro(self, livro):
        if not livro.emprestado and livro in self.catalogo:
            livro.emprestado = True
            print('Livro emprestado com sucesso!')
        else:
            print('Livro indisponível ou emprestado')

    def devolver_livro(self, livro):
        if livro.emprestado:
            livro.emprestado = False
            print('Livro devolvido com sucesso')



def menu():
    print('Escolha sua opção:')
    print('1 - Cadastrar usuário')
    print('2 - Cadastrar livro')
    print('3 - Emprestar livro')
    print('4 - Devolver livro')
    print('5 - Sair do sistema')

    biblioteca = Biblioteca('Angra Reis', 'Rua são paulo')

    opcao = input('Digite sua opcao: ')
    
    if opcao == '1':
        try:
            nome = input('Insira seu nome: ')
            sobrenome = input('Insira seu sobrenome: ')
            matricula = input('Insira sua matricula')
            endereço = input('Insira seu endereço: ')
            cpf = input('Insira seu cpf: ')
            data_de_nascimento = input('Insira sua data de nascimento: ')
            funcao = input('Insira sua função na biblioteca, caso não tenha digite(NÃO): ')
            
            armazenar_pessoa = Pessoa(nome,sobrenome,matricula,endereço,cpf,data_de_nascimento,funcao)
            biblioteca.cadastrar_usuarios(armazenar_pessoa)
        
        except ValueError:
            return print('Você inseriu um valor invalido. ')
        
        
    if opcao == '2':
        try:
            titulo = input('Insira o titulo do livro: ')
            autor = input('Insira o nome do autor: ')
            ano = input('Insira o ano do livro: ')
            categoria = input('Insira a categoria do livro: ')
            editora = input('Insira a editora do livro: ')
            ISBN = input('Insira o ISBN do livro: ')
            
            armazenar_livro = Livro(titulo,autor,ano,categoria,editora,ISBN)
            biblioteca.cadastrar_livros(armazenar_livro)
        
        except ValueError:
            return print('Você inseriu um valor invalido. ')
    
    if opcao == '3':
        try:
            emprestar_livro = input('Insira o nome do livro que deseja: ')
            
            for livro in biblioteca.catalogo:
                if emprestar_livro == livro:
                    biblioteca.emprestar_livro(emprestar_livro)
                    print('Vocẽ pegou um livro emprestado.')
                    
        except ValueError:
            return print('Você inseriu um valor invalido. ')

    if opcao == '4':
        