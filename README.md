# Agriness CMS API

Aplicação desenvolvida em **Django Rest Framework** para um simples gerenciador de conteúdo onde será possível cadastrar 
incríveis textos para leitura futura.

Este é o projeto da API backend do Agriness - CMS. A utilização destes serviços pode ser feita utilizando o projeto 
https://github.com/mateusvsv/agriness-cms.

## Requisitos

- Python 3.5+
- virtualevn

## Preparando o Projeto

Com os requisitos instalados nas versões citadas, podemos baixar e configurar o projeto.

Clonando o repositório:
```
git clone git@github.com:mateusvsv/agriness-api.git
```
Entrando no diretório do projeto:
```
cd agriness-api/
```
Criando e ativando ambiente virtual:
```
virtualenv env

source env/bin/activate
```

Instalando as dependências do projeto:
```
pip install -r requirements.txt
```

Criando banco de dados:
```
python manage.py migrate
```
Esta aplicação utiliza Sqlite3, não sendo necessário configurar conexão externa com outro banco de dados.

## Executando testes

Para verificar o funcionamento básico da API foram implementados testes unitários dos principais serviços.
Os testes podem ser executados com:
```
python manage.py test
```
É importante que os testes sejam executados com sucesso para utilização da API.


## Executando

Uma vez configurado o projeto pode ser executado com o seguinte comando e estará disponível no endereço **http://127.0.0.1:8000/**.
```
python manage.py runserver
```

### Implementações Futuras

- Implementação de Makefile
- Busca por termos do artigo.
- Validações e mensagens ao usuário.