import redis
import os
r = redis.Redis(host='localhost', port=6379, db=0)

def redis_use(code, original_url, expire_seconds=5):
    r.setex(f"short:{code}", expire_seconds, original_url)

def redis_get(code):
    value = r.get(f"short:{code}")
    if value is None:
        return None
    return value.decode('utf-8')

#debug
print(r.set('foo', 'bar'))
print(r.get('foo'))
print(r.expire("test", 10))