registros_alunos = [
    {
        "nome": "João Silva",
        "idade": 15,
        "classe": "9º ano",
        "notas": {"Matemática": 85, "Português": 78, "Ciências": 92, "História": 93}
    },
    {
        "nome": "Maria Oliveira",
        "idade": 14,
        "classe": "8º ano",
        "notas": {"Matemática": 90, "Português": 82, "Ciências": 88, "História": 84}
    },
    {
        "nome": "Carlos Santos",
        "idade": 16,
        "classe": "9º ano",
        "notas": {"Matemática": 78, "Português": 80, "Ciências": 75, "História": 78}
    },
    {
        "nome": "Ana Pereira",
        "idade": 15,
        "classe": "9º ano",
        "notas": {"Matemática": 92, "Português": 85, "Ciências": 90, "História": 88}
    },
    {
        "nome": "Pedro Costa",
        "idade": 14,
        "classe": "8º ano",
        "notas": {"Matemática": 88, "Português": 79, "Ciências": 84, "História": 80}
    }
]


while True:
    print("\n===== SISTEMA ESCOLAR =====")
    print("1 - Cadastrar novo aluno")
    print("2 - Exibir todos os alunos")
    print("3 - Sair")
    
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        novo_aluno = {}

        
        novo_aluno["nome"] = input("Digite o nome do aluno: ")
        novo_aluno["idade"] = int(input("Digite a idade do aluno: "))
        novo_aluno["classe"] = input("Digite a classe do aluno: ")
        novo_aluno["notas"] = {}

        
        while True:
            materia = input("Digite o nome da matéria (ou 'sair' para finalizar): ")
            if materia.lower() == "sair":
                break
            nota = int(input(f"Digite a nota de {materia}: "))
            novo_aluno["notas"][materia] = nota

        
        registros_alunos.append(novo_aluno)
        print(f"Aluno {novo_aluno['nome']} cadastrado com sucesso!")

    elif escolha == "2":
        print("\n===== LISTA DE ALUNOS =====")
        for aluno in registros_alunos:
            print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Classe: {aluno['classe']}, Notas: {aluno['notas']}")
    
    elif escolha == "3":
        print("Saindo do sistema...")
        break
    
    else:
        print("Opção inválida! Tente novamente.")
