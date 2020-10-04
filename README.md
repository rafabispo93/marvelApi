# Python Developer - Dextra: Marvel API

# Download

Para utilizar o projeto é necessário ter os programas abaixo instalados:

    1. Docker
    2. Docker-Compose
        Ambos acima encontrados aqui https://www.docker.com/products
    3. Python (https://www.python.org/)

# Repositório


Faça o clone do repositório com o comando

```sh
    git clone https://github.com/rafabispo93/marvelApi.git
```

# Build

Após ter feito o clone siga os passos seguintes:

    1. Abra a pasta do projeto
    2. Rode o comando docker-compose up -d
    3. Após isso rode o comando python /startup/db_start.py

# Testes

Para rodar os testes unitários rode os comandos abaixo

```bash
    docker exec -it marvelapi_web_1 bash
    python tests.py
```

# Acesso

Após esses passos a API estará disponível na url http://localhost:5000