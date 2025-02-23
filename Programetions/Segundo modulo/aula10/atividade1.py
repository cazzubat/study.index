import os

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



def continue1():
        continue1 = (input('Você deseja voltar ao menu: Y/N ')).lower()
        if continue1 == 'y':
            return menu()
        else:
            print("\n" * os.get_terminal_size().lines)
            return print('Você saiu do menu.')

biblioteca = Biblioteca('Angra Reis', 'Rua são paulo')

def verificar_status_livro():
    escolher_livro = input('Insira o título do livro que deseja verificar: ').strip().lower()

    if not biblioteca.catalogo:  # Verifica se há livros cadastrados
        print('O catálogo está vazio.')
        return

    livro_encontrado = False  # Variável para rastrear se o livro foi encontrado

    for livro in biblioteca.catalogo:
        if livro.titulo.lower() == escolher_livro:
            livro_encontrado = True  
            status = "emprestado" if livro.emprestado else "disponível"
            print(f'O livro "{livro.titulo}" está {status}.')
            break  

    if not livro_encontrado:  
        print('Não temos esse livro no catálogo.')


def menu():
    print('Escolha sua opção:')
    print('1 - Cadastrar usuário')
    print('2 - Cadastrar livro')
    print('3 - Emprestar livro')
    print('4 - Devolver livro')
    print('5 - Sair do sistema')
    print('6 - Status do livro')

    opcao = input('Digite sua opcao: ')
    
    if opcao == '1':
        try:
            nome = input('Insira seu nome: ')
            sobrenome = input('Insira seu sobrenome: ')
            matricula = input('Insira sua matricula: ')
            endereço = input('Insira seu endereço: ')
            cpf = input('Insira seu cpf: ')
            data_de_nascimento = input('Insira sua data de nascimento: ')
            funcao = input('Insira sua função na biblioteca, caso não tenha digite (NÃO): ')
            
            armazenar_pessoa = Pessoa(nome,sobrenome,matricula,endereço,cpf,data_de_nascimento,funcao)
            biblioteca.cadastrar_usuarios(armazenar_pessoa)
        
        except ValueError:
            return print('Você inseriu um valor invalido. ')
        
        continue1()
        
    elif opcao == '2':
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

        continue1()

    elif opcao == '3':
        try:
            emprestar_livro = input('Insira o título do livro que deseja: ')
            
            for livro in biblioteca.catalogo:
                if livro.titulo.lower() == emprestar_livro.lower():
                    if not livro.emprestado: 
                        biblioteca.emprestar_livro(livro)
                        print(f'Você pegou o livro "{livro.titulo}" emprestado.')
                    else:
                        print(f'O livro "{livro.titulo}" está emprestado.')
                    break
            else:
                print('Não temos esse livro no catálogo.')

        except ValueError:
            return print('Você inseriu um valor inválido. ')

        continue1()

    elif opcao == '4':
        try:
            devolver_livro = input('Digite o título do livro que deseja devolver: ')

            for livro in biblioteca.catalogo:
                if livro.titulo.lower() == devolver_livro.lower():
                    biblioteca.devolver_livro(livro)
                    print(f'Você devolveu o livro "{livro.titulo}".')
                    break
            else:
                print('Não temos esse livro no catálogo.')

        except ValueError:
            return print('Você inseriu um valor inválido.')

        continue1()

        
    elif opcao == '5':
        return print('Você saiu do menu.')
    
    elif opcao == '6':
        verificar_status_livro()

        continue1()

    else:
        print("\n" * os.get_terminal_size().lines)
        print('Você inseriu um valor invalido.')
        return menu()

menu()
