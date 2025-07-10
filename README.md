## Encurtador de URL Temporário (Flask + Redis)

Projeto simples para encurtar URLs que expiram após 3 dias.

Feito com Flask (backend) e Redis (cache temporário).

Redis rodando via Docker para facilitar o setup.

## Uso

Clone o repositório

Suba o Redis com Docker:
```
docker run --name redis_encurtador -p 6379:6379 -d redis

```

Instale dependências:
```
pip install -r requirements.txt

```

Rode o app:
```
python app.py
```

Acesse:
http://localhost:5000

## Estrutura:
app.py: rotas e lógica principal

redis_client.py: conexão e funções Redis

utils.py: geração dos códigos aleatórios

templates/index.html: interface simples
