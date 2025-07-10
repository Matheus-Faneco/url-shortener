from flask import Flask, request, render_template, redirect
from utils import generate_code
from redis_client import redis_use, redis_get

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def shorten():
    if request.method == 'POST':
        long_url = request.form.get('url', '').strip()

        if not long_url:
            return render_template('index.html', error='Campo de URL vazio')

        if not long_url.startswith(('http://', 'https://')):
            long_url = 'https://' + long_url
        #chamando função para gerar codigo da url
        short_url = generate_code()

        redis_use(short_url, long_url, expire_seconds=10)

        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

@app.route('/<short_url>')
def redirecionar_para_url(short_url):
    original_url = redis_get(short_url)
    if original_url is None:
        return render_template('index.html', error='link expirado')
    return redirect(original_url)
if __name__ == '__main__':
    app.run(debug=True)