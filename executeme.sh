#!/bin/bash

# Instala o ambiente virtual
sudo apt install python3.8-venv

# Cria um ambiente virtual para o projeto
python3 -m venv .venv

# Cria um arquivo chamado "meuarquivo.txt" na pasta do projeto
touch mysite/testing.py

# Adiciona o conteúdoentre aspas ao arquivo testing.py
echo "import os

secretkey = 'django-insecure-mwn_yn^f))myqf-9v(r=7dz1+v0nm4*g@9@b!(#kpo&@ww#41a'

database = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db.sqlite3'),
    }
}" > mysite/testing.py
