import sqlite3

# Conecta ao banco de dados
conexao = sqlite3.connect('banco_de_dados.db')


# Cria um cursor para executar comandos SQL
cursor = conexao.cursor()

# Cria a tabela usuarios se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nome VARCHAR,
    email VARCHAR
);
''')

# Puxar informações do banco de dados
result = cursor.fetchall()

# Inserir dados na tabela
def cadastra_usuario(nome, email):
    sql = "INSERT INTO usuarios (nome, email) VALUES (?, ?)"
    cursor.execute(sql, (nome, email))
    conexao.commit() 

cadastra_usuario('Thiago', 'oshirothiago@gmail.com')
 
# Mostrar todos os dados da tabela
def mostrar_usuarios():
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()
    
    sql = "SELECT * FROM usuarios"
    cursor.execute(sql)
    
    usuarios = cursor.fetchall()
    
    for usuario in usuarios:
        print(usuario)
    
    conexao.close()

mostrar_usuarios()

# Usa uma query segura com parâmetros
def selecionar_usuario(id):
    sql = "SELECT * FROM usuarios WHERE id = ?"
    cursor.execute(sql, (id,))
    result = cursor.fetchall()
    print(result)


print('-'*20)
selecionar_usuario(20)
# Imprime os resultados
for linha in result:
    print(linha)

# Atualiza dados na tabela
def atualizar_user(nome,id):
    sql = "UPDATE usuarios SET nome = ? WHERE id = ?"
    cursor.execute(sql, (nome,id))
    conexao.commit()
    result

atualizar_user('joaozinho',74)

# Exclui dados da tabela
def apagar_usuarios(id):
    sql = "DELETE FROM usuarios WHERE id = ?"
    cursor.execute(sql, (id,))
    conexao.commit()
    result

apagar_usuarios(74)

# Fecha a conexão com o banco de dados
conexao.close()