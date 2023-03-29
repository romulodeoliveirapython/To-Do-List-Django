#!/bin/bash


# Cria um ambiente virtual para o projeto
python3 -m venv .venv

# Ativa o ambiente virtual
source .venv/bin/activate

# Instala as dependências do projeto
python -m pip install -r requirements.txt

# Executa as migrações do banco de dados
python manage.py makemigrations
python manage.py migrate

# Exibe uma mensagem em vermelho
echo -e "\033[31mAGORA CRIE SEU USUÁRIO E SENHA\033[0m"

# Cria um superusuário para o Django
python manage.py createsuperuser

# Cria um arquivo chamado "meuarquivo.txt" na pasta do projeto
touch mysite/testing.py

# Adiciona o conteúdo "Este é o conteúdo do meu arquivo" ao arquivo
echo "secretkey = 'django-insecure-mwn_yn^f))myqf-9v(r=7dz1+v0nm4*g@9@b!(#kpo&@ww#41a'

database = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}" > mysite/testing.py

# Executa o servidor web do Django e abre o navegador no link 127.0.0.1:8000/
python manage.py runserver & xdg-open http://127.0.0.1:8000/