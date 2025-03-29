# Comandos para rodar o Flet como web app no Linux

# 1. Primeiro, crie e ative um ambiente virtual no seu terminal:
# (Se você não fez isso ainda, siga as instruções anteriores)

# Criar o ambiente virtual:
python3 -m venv flet-env

# Ativar o ambiente virtual:
source flet-env/bin/activate

# 2. Instale o Flet dentro do ambiente virtual:
pip install flet

# 3. Agora, para rodar seu código Python como um web app com o Flet:
flet run --web flet2.py

# Explicação:
# O comando 'flet run --web flet2.py' vai iniciar o seu código Python (flet2.py) e 
# rodá-lo como uma aplicação web, acessível em um navegador.
