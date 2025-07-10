import redis
r = redis.Redis(host='localhost', port=6379, db=0)

def redis_use(codigo, original_url, segundos_expiracao=10):
    r.setex(f"short:{codigo}", segundos_expiracao, original_url)  #setex -> set with expire
    #3 parametros estao sendo passados: name, time, value(codigo, original_url, segundos_expiracao=10)
    #na teoria, os parametros deveriam estar nesta ordem: codigo, segundos_expiracao=10, original_url
    #no entanto, o código para de fucionar por algum motivo.

def redis_get(codigo):
    value = r.get(f"short:{codigo}")
    if value is None:
        return None
    return value.decode('utf-8')

#teste de conexão
# print(r.set('foo', 'bar'))
# print(r.get('foo'))
# print(r.expire("test", 10))