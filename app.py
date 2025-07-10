from flask import Flask, request, render_template, redirect
from utils import gerar_codigo_url_encurtada
from redis_client import salvar_url_encurtada, buscar_url_original

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def encurtar_url():
    if request.method == 'POST':
        url_longa = request.form.get('url', '').strip()

        if not url_longa:
            return render_template('index.html', error='O campo de URL está vazio.')

        if not url_longa.startswith(('http://', 'https://')):
            url_longa = 'https://' + url_longa

        # gera código aleatório para a URL encurtada
        codigo_encurtado = gerar_codigo_url_encurtada()

        # salva no Redis com tempo de expiração
        salvar_url_encurtada(codigo_encurtado, url_longa)

        return render_template('index.html', short_url=codigo_encurtado)

    return render_template('index.html')

@app.route('/<codigo_encurtado>')
def redirecionar(codigo_encurtado):
    # chama a função buscar_url_original
    url_original = buscar_url_original(codigo_encurtado)

    if url_original is None:
        return render_template('index.html', error='Link expirado ou inválido.')

    return redirect(url_original)

if __name__ == '__main__':
    app.run()
