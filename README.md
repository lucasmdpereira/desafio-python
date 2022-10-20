# Sumário

1. [Objetivo](#objetivo)
2. [Tecnologias](#tecnologias)
3. [Estrutura de pastas](#estrutura-de-pastas)
4. [Iniciar Aplicação](#iniciar-aplicação)
5. [Classes](#classes)

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
    python3 src/index.py
```

## Classes

### getDataFromAPI

Classe responsável por receber os dados da API e manipular os dados recebidos
através de seus métodos:

```python
    GetData() # retorna todos os dados da API
    GetWebsites() # retorna todos os websites
    GetNameEmailCompany() # retorna todos os nomes, emails e empresas
    GetUserByNameSearch("query") # retorna nomes encontrados que contenham "query"
```
