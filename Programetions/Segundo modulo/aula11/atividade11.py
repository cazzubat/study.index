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
            'autor': self.autor,
            'ano': self.ano,
            'categoria': self.categoria,
            'editora': self.editora
        }
    
class Pessoa:
    def __init__(self, nome, sobrenome, matricula, endereco, cpf, funcao:False):
        self.nome = nome
        self.sobrenome = sobrenome
        self.matricula = matricula
        self.endereco = endereco
        self.cpf = cpf
        self.funcao = funcao
        self.emprestimos = []

    def emprestimos_para_string(self):
        return ", ".join(livro.titulo for livro in self.emprestimos) if self.emprestimos else "Nenhum empréstimo registrado"

    
    def get_dict_user(self):
        dicionario = {
            'nome': self.nome.capitalize(),
            'sobrenome': self.sobrenome.capitalize(),
            'matricula': self.matricula,
            'endereco': self.endereco,
            'cpf': self.cpf,
            'funcao': 'Funcionário' if self.funcao else 'Cliente',
            'emprestimos': self.emprestimos_para_string()
        }
        return dicionario

    def get_emprestimos(self):
        emprestados = []
        for livro in self.emprestimos:
            emprestados.append(livro.get_dict())
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

    def cadastrar_funcionario(self, usuario: Pessoa):
        self.funcionarios.append(usuario)        
    
    def emprestar_livro(self, usuario_nome: str, livro_titulo: str):
        pessoa = next((verificar for verificar in self.usuarios if verificar.nome == usuario_nome), None)
        livro = next((verificar1 for verificar1 in self.catalogo if verificar1.titulo == livro_titulo), None)

        if pessoa is None:
            print('Usuário não cadastrado')
        elif livro is None:
            print('Livro não registrado')
        elif livro.emprestado:
            print('Este livro já está emprestado')
        else:
            livro.emprestado = True
            pessoa.emprestimos.append(livro)
            print(f'Livro "{livro.titulo}" emprestado com sucesso para {pessoa.nome.capitalize()}!')

    def cadastrar_livros(self, livro: Livro):
        self.catalogo.append(livro)
        print('Livro cadastrado com sucesso!') 

    def devolver_livro(self, usuario_pessoa: str, titulo_livro: str):
        pessoa = next((verificar2 for verificar2 in self.usuarios if verificar2.nome == usuario_pessoa), None)
        livro = next((verificar3 for verificar3 in self.catalogo if verificar3.titulo == titulo_livro), None)

        if pessoa is None:
            print('Usuário não cadastrado')
        elif livro is None:
            print('Livro não registrado')
        elif livro not in pessoa.emprestimos:
            print('Este livro não está emprestado para este usuário')
        else:
            livro.emprestado = False
            pessoa.emprestimos.remove(livro)
            print(f'{usuario_pessoa.capitalize()} seu livro "{titulo_livro}" foi devolvido com sucesso.')

def continue1():
    continuar = input('Você deseja voltar ao menu? (S/N) ').lower()
    if continuar == 's':
        return menu()
    else:
        print('Você saiu do menu.')

biblioteca = Biblioteca('Angras', 'Rua Reis')

def menu():
    print('Lista para o Gerenciador da Empresa.')
    print('Escolha uma das opções abaixo:')
    print('1 - Cadastrar usuário')
    print('2 - Ver usuários cadastrados')
    print('3 - Cadastrar livro')
    print('4 - Ver livros cadastrados')
    print('5 - Emprestar livro')
    print('6 - Devolver livro')
    print('7 - Remover usuario')
    print('8 - Remover livro')
    print('9 - Sair do sistema')

    opcao = input('Digite sua opção: ')

    if opcao == '1':
        try:
            nome = input('Nome: ').lower().strip()
            sobrenome = input('Sobrenome: ').lower().strip()
            matricula = input('Matrícula: ').lower().strip()
            endereco = input('Endereço: ').lower().strip()
            cpf = input('CPF: ').lower().strip()
            funcao = input('Você é funcionário? (S/N) ').lower().strip()
            
            funcao = True if funcao == 's' else False
            
            armazenar_pessoa = Pessoa(nome, sobrenome, matricula, endereco, cpf, funcao)
            
            if funcao == True:
                biblioteca.cadastrar_funcionario(armazenar_pessoa)
            
            biblioteca.cadastrar_usuarios(armazenar_pessoa)
        
        except ValueError:
            print('Você inseriu um valor inválido.')
        
        continue1()

    elif opcao == '2':
        if biblioteca.usuarios:
            for usuario in biblioteca.usuarios:
                print(usuario.get_dict_user())
        else:
            print('Não há nenhum usuário cadastrado.')
    
        continue1()
    
    elif opcao == '3':
        try:
            titulo = input('Insira o título do livro: ').lower().strip()
            autor = input('Insira o nome do autor: ').lower().strip()
            ano = input('Insira o ano do livro: ').lower().strip()
            categoria = input('Insira a categoria do livro: ').lower().strip()
            editora = input('Insira a editora do livro: ').lower().strip()
            
            armazenar_livro = Livro(titulo, autor, ano, categoria, editora)
            biblioteca.cadastrar_livros(armazenar_livro)
        
        except ValueError:
            print('Você inseriu um valor inválido.')

        continue1()

    elif opcao == '4':
        if biblioteca.catalogo:
            for livro in biblioteca.catalogo:
                print(livro.get_dict())
        else:
            print('Não há nenhum livro cadastrado.')
       
        continue1()
    
    elif opcao == '5':
        try:
            usuario_encontrado = input('Insira o seu nome: ').lower().strip()
            livro_encontrado = input('Insira o título do livro desejado: ').lower().strip()
            biblioteca.emprestar_livro(usuario_encontrado, livro_encontrado)
        
        except ValueError:
            print('Você inseriu um valor inválido.')
        
        continue1()
    
    elif opcao == '6':
        try:
            usuario_pessoa = input('Insira o seu nome: ').lower().strip()
            livro_achado = input('Insira o título do livro que deseja devolver:  ').lower().strip()
            biblioteca.devolver_livro(usuario_pessoa, livro_achado)
        
        except ValueError:
            print('Você inseriu um valor inválido.')

        continue1()
    
    elif opcao == '7':
        try:
            for i, usuario in enumerate(biblioteca.usuarios, start=1):
                print(f'Índice {i} - {usuario.get_dict_user()}')
            
            print('-'*10)

            indice = int(input('Escolha pelo índice o usuário que deseja remover: '))

            if 1 <= indice <= len(biblioteca.usuarios):
                biblioteca.usuarios.pop(indice - 1)
                print("Usuário removido com sucesso!")
            else:
                print("Índice inválido!")
        except ValueError:
            print('Você inseriu um valor inválido.')        

        continue1()
    
    elif opcao == '8':
        try:
            for i, livro in enumerate(biblioteca.catalogo, start=1):
                print(f'Índice {i} - {livro.get_dict()}')
            
            print('-'*10)

            indice = int(input('Escolha pelo índice o livro que deseja remover: '))

            if 1 <= indice <= len(biblioteca.catalogo):
                biblioteca.catalogo.pop(indice - 1)
                print("Livro removido com sucesso!")
            else:
                print("Índice inválido!")
        except ValueError:
            print('Você inseriu um valor inválido.')         

        continue1()

    elif opcao == '9':
        return print('Você saiu do menu.')
    
    else:
        print('Você inseriu um valor invalido.')
        return menu()
        
menu()
