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

## Referências

- [How to Build a URL Shortener with Go (Dev.to)](https://dev.to/envitab/how-to-build-a-url-shortener-with-go-5hn5)  
- [Python Tutorial: How to Create a URL Shortener with Flask (TheLinuxCode)](https://thelinuxcode.com/python-tutorial-how-to-create-a-url-shortener-with-flask/)  
- [Redis Python Client (redis-py) - PyPI](https://pypi.org/project/redis/)
- [Redis Python Examples (Official docs](https://redis.readthedocs.io/en/stable/examples.html)


