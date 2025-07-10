import redis
# conectando ao Redis local
cliente_redis = redis.Redis(host='localhost', port=6379, db=0)

def salvar_url_encurtada(codigo, url_original, segundos_expiracao=259200):  # 3 dias
    # salva a URL original no Redis com tempo de expiração
    cliente_redis.setex(f"encurtada:{codigo}", segundos_expiracao, url_original)  # setex = set with expire

def buscar_url_original(codigo):
    # busca a URL original a partir do código encurtado
    valor = cliente_redis.get(f"encurtada:{codigo}")
    if valor is None:
        return None
    return valor.decode('utf-8')

# testes manuais (descomente para usar)
# print(cliente_redis.set('teste', 'valor'))
# print(cliente_redis.get('teste'))
# print(cliente_redis.expire('teste', 10))
