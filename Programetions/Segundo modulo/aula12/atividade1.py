#SISTEMA DE HAMBURGUERIA:
#"Estou querendo criar um sistema pra minha hamburgueria...
#Vou precisar de um cardápio, um sistema de fidelização de clientes,
#e um jeito pra pessoa poder fazer pedido e vir aqui pegar ou mandar motoboy entregar?
#E aí você conseque fazer até semana que vem?"

class item_cardapio:
    def __init__(self,pao,carne,salada,molho,nome,preço=float):
        self.pao = pao
        self.carne = carne
        self.salada = salada
        self.molho = molho
        self.nome = nome
        self.preço = preço

    def get_dict_cardapio(self):
        return{
            'Pão': self.pao.capitalize(),
            'Carne': self.carne.capitalize(),
            'Salada': self.salada.capitalize(),
            'Molho': self.molho.capitalize(),
            'Nome': self.nome.capitalize(),
            'Preço': self.preço
        }

class Cliente:
    def __init__(self,nome,cpf=int,endereço=str,fidelizacao=False):
        self.nome = nome
        self.cpf = cpf
        self.endereço = endereço
        self.pedidos = []
        self.fidelizacao = fidelizacao

    def get_dict_cliente(self):
        dicionario = {
            'Nome': self.nome.capitalize(),
            'CPF': self.cpf,
            'Endereço': self.endereço,
            'Pedidos': self.pedidos_para_string(),
            'Fidelização': 'Esse cliente é fidelizado' if self.fidelizacao_cliente() else 'Esse cliente não é fidelizado'
        }
        return dicionario 
    
    def fidelizacao_cliente(self):
        quantidade_pedidos = len(self.pedidos)
        if quantidade_pedidos >= 2:
                self.fidelizacao = True
                return True
        return False


    def pedidos_para_string(self):
        return ", ".join(pedido.nome for pedido in self.pedidos) if self.pedidos else "Nenhum pedido registrado"

class Funcinario:
    def __init__(self,nome,cpf=int,senha=str):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha

    def get_dict_funcionario(self):
        return{
            'Nome': self.nome.capitalize(),
            'CPF': self.cpf,
            'Senha': self.senha
        }

class Restaurante:
    def __init__(self,nome,horario_fucionamento,):
        self.nome = nome
        self.horario_fucionamento = horario_fucionamento
        self.funcionarios = []
        self.clientes = []
        self.cardapio = []
    
    def adicionar_fucionarios(self,funcionario:Funcinario):
        self.funcionarios.append(funcionario)
        print('Funcionario cadastrado com sucesso.')
    
    def adicionar_clientes(self,cliente:Cliente):
        self.clientes.append(cliente)
        print('Cliente cadastrado com sucesso.')
    
    def adicionar_cardapio(self,item:item_cardapio):
        self.cardapio.append(item)
        print('Item foi adicionado com sucesso em cardapio.')

    def fazer_pedido(self, cliente: Cliente):
        try:
            if cliente is None:
                print("Não existe esse cliente.")
                return
            if not self.cardapio:
                print("O cardápio está vazio.")
                return
            for i, pedido in enumerate(self.cardapio, start=1):
                print(f'Índice {i} - {pedido.get_dict_cardapio()}')
                print('-' * 10)

            indice = int(input('Escolha pelo índice o pedido que deseja: '))
        
            if 1 <= indice <= len(self.cardapio):
                pedido_escolhido = self.cardapio[indice - 1] 
                cliente.pedidos.append(pedido_escolhido) 
                print("Pedido realizado com sucesso!")
            else:
                print("Índice inválido!")
        
        except ValueError:
            print("Valor inválido.")


    def remover_fucionarios(self,indice=int):
        try:
            if not self.funcionarios:  
                print("Não há funcionarios cadastrados.")
                return
            else:
                print("Lista de funcionários:")
                for i, usuario in enumerate(self.funcionarios, start=1):
                    print(f'Índice {i} - {usuario.get_dict_funcionario()}')
                    print('-'*10)
                    
                indice = int(input('Escolha pelo índice o funcionario que deseja remover: '))
                if 1 <= indice <= len(self.funcionarios):
                    self.funcionarios.pop(indice - 1)
                    print("Usuário removido com sucesso!")
                else:
                    print("Índice inválido!")
        except ValueError:
            print('Valor inválido.')

    def remover_cliente(self,indice=int):
        try:
            if not self.clientes:
                print("Não há clientes cadastrados.")
                return
            else:
                for i, usuario in enumerate(self.clientes, start=1):
                    print(f'Índice {i} - {usuario.get_dict_cliente()}')
                    print('-'*10)
                    
                indice = int(input('Escolha pelo índice o funcionario que deseja remover: '))
                if 1 <= indice <= len(self.clientes):
                        self.clientes.pop(indice - 1)
                        print("Usuário removido com sucesso!")
                else:
                    print("Índice inválido!")
        except ValueError:
            print('Valor inválido.')
    
    def remover_item_cardapio(self,indice=int):
        try:
            if not self.cardapio:
                print("Não há nenhum item cadastrados.")
                return
            else:
                for i, usuario in enumerate(self.funcionarios, start=1):
                    print(f'Índice {i} - {usuario.get_dict_cardapio()}')
                    print('-'*10)
                
                indice = int(input('Escolha pelo índice o funcionario que deseja remover: '))
                if 1 <= indice <= len(self.funcionarios):
                    self.funcionarios.pop(indice - 1)
                    print("Usuário removido com sucesso!")
                else:
                    print("Índice inválido!")
        except ValueError:
            print('Valor inválido.')

def continue1():
    continuar = input('Você deseja voltar ao menu? (S/N) ').lower()
    if continuar == 's':
        print('\n')
        return menu()
    else:
        print('Você saiu do menu.')

restaurante = Restaurante('Restaurante', '12:00 até 20:00')

def menu():
    print('Escolha uma das opções abaixo:')
    print('1 - Cadastrar cliente')
    print('2 - Informações do cliente')
    print('3 - Cadastrar funcionario')
    print('4 - Ver funcionarios cadastrados')
    print('5 - Cadastrar item no cardapio')
    print('6 - Ver item no cardapio')
    print('7 - Fazer um pedido')
    print('8 - Remover cliente')
    print('9 - Remover funcionario')
    print('10 - Remover item no cardapio')
    print('11 - Sair do sistema')

    opcao = input('Digite sua opção: ').strip()
        
    if opcao == '1':
        try:
            nome = input('Nome: ').lower().strip()
            cpf = int(input('CPF: '))
            endereço = input('Endereço: ').lower().strip()
            
            armazenar_cliente = Cliente(nome,cpf,endereço)
            restaurante.adicionar_clientes(armazenar_cliente)
        except ValueError:
            print('Você inseriu um valor invalido.')
        
        continue1()

    elif opcao == '2':
        if not restaurante.clientes:
            print('Não há nenhum cliente cadastrado.')
        else:
            for user in restaurante.clientes:
                print(user.get_dict_cliente())

        continue1()

    elif opcao == '3':
        try:
            nome = input('Nome: ').lower().strip()
            cpf = int(input('CPF: '))
            senha = input('Senha: ').lower().strip()
            
            armazenar_funcionario = Funcinario(nome,cpf,senha)
            restaurante.adicionar_fucionarios(armazenar_funcionario)
        except ValueError:
            print('Você inseriu um valor invalido.')
        
        continue1()
    
    elif opcao == '4':
        if restaurante.funcionarios:
            for user in restaurante.funcionarios:
                print(user.get_dict_funcionario())
        else:
            print('Não há nenhum funcionarios cadastrado.')
        
        continue1()
    
    elif opcao == '5':
        print('Insira o seu login de funcionario: ')
        print('\n')
        try:
            nome = input('Nome: ')
            cpf = int(input('CPF: '))
            senha = input('Senha: ')
        except ValueError:
            print('Você inseriu um valor invalido.')
            continue1()

        validar_funcionario = Funcinario(nome, cpf, senha)

        if any(
            funcionario.cpf == validar_funcionario.cpf and 
            funcionario.nome == validar_funcionario.nome and 
            funcionario.senha == validar_funcionario.senha 
            for funcionario in restaurante.funcionarios
        ):
            try:
                pao = input('Pão: ').lower().strip()
                carne = input('Carne: ').lower().strip()
                molho = input('Molho: ').lower().strip() 
                salada = input('Salada: ').lower().strip()
                nome = input('Nome: ').lower().strip()
                preço = float(input('Preço: '))

                armazenar_item_cardapio = item_cardapio(pao,carne, molho, salada, nome, preço)
                restaurante.adicionar_cardapio(armazenar_item_cardapio)
            except ValueError:
                print('Você inseriu um valor invalido.')
        else:
            print('Não há nenhum funcionario cadastrado ou você inseriu um valor invalido.')

        continue1()

    
    elif opcao == '6':
        if restaurante.cardapio:
            for item in restaurante.cardapio:
                print(item.get_dict_cardapio())
        else:
            print('Não há nenhum item no cardapio.')
        
        continue1()
    
    elif opcao == '7':
        print('Insira suas informações de cliente:')
        print('\n')
        try:
            nome = input('Nome: ')
            cpf = int(input('CPF: '))
            endereço = input('Endereço: ')
        except ValueError:
            print('Você inseriu um valor inválido.')
            continue1()

        cliente_encontrado = next(
            (cliente for cliente in restaurante.clientes if cliente.cpf == cpf and cliente.nome == nome and cliente.endereço == endereço),
            None
        )

        if cliente_encontrado:
            restaurante.fazer_pedido(cliente_encontrado)
        else:
            print('Não há nenhum cliente cadastrado com esses dados ou você inseriu um valor inválido.')

        continue1()
    
    elif opcao == '8':
        print('Insira o seu login de funcionario: ')
        print('\n')
        try:
            nome = input('Nome: ')
            cpf = int(input('CPF:'))
            senha = input('Senha: ')
        except ValueError:
                print('Você inseriu um valor invalido.')

        validar_funcionario = Funcinario(nome,cpf,senha)
        
        if any(
        funcionario.cpf == validar_funcionario.cpf and 
        funcionario.nome == validar_funcionario.nome and 
        funcionario.senha == validar_funcionario.senha 
        for funcionario in restaurante.funcionarios
        ):        
            restaurante.remover_cliente()
        
        else:
            print('Não há nenhum funcionarios cadastrado ou você inseriu um valor invalido.')
    
        continue1()
    
    elif opcao == '9':
        print('Insira o seu login de funcionario: ')
        print('\n')
        try:
            nome = input('Nome: ')
            cpf = int(input('CPF:'))
            senha = input('Senha: ')
        except ValueError:
                print('Você inseriu um valor invalido.')

        validar_funcionario = Funcinario(nome,cpf,senha)

        if any(
        funcionario.cpf == validar_funcionario.cpf and 
        funcionario.nome == validar_funcionario.nome and 
        funcionario.senha == validar_funcionario.senha 
        for funcionario in restaurante.funcionarios
        ):        
            restaurante.remover_fucionarios()
        
        else:
            print('Não há nenhum funcionarios cadastrado ou você inseriu um valor invalido.')
    
        continue1()

    elif opcao == '10':
        print('Insira o seu login de funcionario: ')
        print('\n')
        try:
            nome = input('Nome: ')
            cpf = int(input('CPF:'))
            senha = input('Senha: ')
        except ValueError:
                print('Você inseriu um valor invalido.')

        validar_funcionario = Funcinario(nome,cpf,senha)

        if any(
        funcionario.cpf == validar_funcionario.cpf and 
        funcionario.nome == validar_funcionario.nome and 
        funcionario.senha == validar_funcionario.senha 
        for funcionario in restaurante.funcionarios
        ):        
            restaurante.remover_item_cardapio()
        
        else:
            print('Não há nenhum funcionarios cadastrado ou você inseriu um valor invalido.')
    
        continue1()

    elif opcao == '11':
        return print('Você saiu do menu.')

    else:
        print('Você inseriu um valor invalido.')
        return menu()

menu()
