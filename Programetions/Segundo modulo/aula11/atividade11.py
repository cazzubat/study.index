import os

class Livro:
    def __init__(self, titulo, autor, ano, categoria, editora):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.categoria = categoria
        self.editora = editora
        self.emprestado = False

    def __str__(self):
        return self.titulo
    
    def get_dict(self):
        return {
            'titulo': self.titulo,
            'autor':  self.autor,
            'ano': self.ano,
            'categoria': self.categoria,
            'editora': self.editora
        }
    
class Pessoa:
    def __init__(self, nome, sobrenome, matricula, endereco, cpf, funcao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.matricula = matricula
        self.endereco = endereco
        self.cpf = cpf
        self.status = True
        self.funcao = funcao
        self.emprestimos = []

    def get_emprestimos(self):
        emprestados = []
        for livros in self.emprestimos:
            emprestados.append(livros.get_dict())
        return emprestados

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

    def emprestar_livro(self, livro, pessoa):
        if pessoa not in self.usuarios:
            print('Usuário não cadastado')
        elif livro.emprestado:
            print('Este livro já está emprestado')
        elif livro not in self.catalogo:
            print('Livro não registrado')
        else:
            livro.emprestado = True
            pessoa.emprestimos.append(livro)
            print(f'Livro emprestado com sucesso! Para usuario {pessoa.nome}')

    def devolver_livro(self, livro, pessoa):
        if livro.emprestado:
            livro.emprestado = False
            print('Livros emprestados com o usuário:')
            print(pessoa.emprestimos.get_emprestimos())
            pessoa.emprestimos.remove(livro)

            print('Livro devolvido com sucesso')

def continue1():
        continue1 = (input('Você deseja voltar ao menu: Y/N ')).lower()
        if continue1 == 'y':
            return menu()
        else:
            return print('Você saiu do menu.')
            


biblioteca = Biblioteca('Angras','Rua Reis')

def menu():
    print('Escolha uma das opções abaixo')
    print('1 - Cadastrar usuário')
    print('2 - Ver usuários cadastrados')
    print('3 - Cadastrar livro')
    print('4 - Ver livros cadastrados')
    print('5 - Emprestar livro')
    print('6 - Devolver livro')
    print('7 - Status do livro')
    print('8 - Área funcionario')
    print('9 - Sair do sistema')

    opcao = input('Digite sua opção: ')

    if opcao == '1':
        try:
            nome = input('Nome: ')
            sobrenome = input('Sobrenome: ')
            matricula = input('Matricula: ')
            endereço = input('Endereço: ')
            cpf = input('CPF: ')
            funcao = input('Você é funcionario: (SIM/NÃO) ')
            
            armazenar_pessoa = Pessoa(nome,sobrenome,matricula,endereço,cpf,funcao)
            biblioteca.cadastrar_usuarios(armazenar_pessoa)
        
        except ValueError:
            return print('Você inseriu um valor invalido. ')
        
        continue1()

    elif opcao == '2':
        print(biblioteca.listar_usuarios)
    
        continue1()
    
    elif opcao == '3':
        try:
            titulo = input('Insira o titulo do livro: ')
            autor = input('Insira o nome do autor: ')
            ano = input('Insira o ano do livro: ')
            categoria = input('Insira a categoria do livro: ')
            editora = input('Insira a editora do livro: ')
            
            armazenar_livro = Livro(titulo,autor,ano,categoria,editora)
            biblioteca.cadastrar_livros(armazenar_livro)
        
        except ValueError:
            return print('Você inseriu um valor invalido. ')

        continue1()
menu()
