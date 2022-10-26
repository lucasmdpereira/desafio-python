# Sumário

- [Sumário](#sumário)
  - [Objetivo](#objetivo)
  - [Tecnologias](#tecnologias)
  - [Estrutura de pastas](#estrutura-de-pastas)
  - [Iniciar aplicação](#iniciar-aplicação)
  - [Classes](#classes)
    - [dataHandler.Data](#datahandlerdata)

## Objetivo

Repositório do [Desafio python #Sangue-Laranja 🍊](./desafio-python.md)

## Tecnologias

Python 3.10.6

## Estrutura de pastas

```shell
    |--src
        |--handlers
```

## Iniciar aplicação

```shell
    pip install -r requirements.txt
    python manage.py runserver
```

## Classes

### dataHandler.Data

Classe responsável por receber os dados da API e manipular os dados recebidos
através de seus métodos:

```python
    list_users_websites # retorna todos os websites
    list_users_name_email_company # retorna todos os nomes, emails e empresas
    list_users_by_query("query") # retorna nomes encontrados que contenham "query"
```
