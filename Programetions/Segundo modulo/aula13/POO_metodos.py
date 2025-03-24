# Teste com metodos da classe

class Login:
    def __init__(self, name, password):
        self.name = name
        self.password = password  

    def __repr__(self):
        return f"Login(nome: '{self.name}', senha: '{self.password}')"

    def __eq__(self, other):
        if isinstance(other, Login):
            return self.name == other.name and self.password == other.password
        return False


login1 = Login('Pedro', '123')
login2 = Login('Pedro', '133')


print(login1 == login2)
print(login1)