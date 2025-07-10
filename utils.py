import random
import string

#função para geração de codigo aleatorio de 6 caracteres
def gerar_codigo_url_encurtada():
    caracteres = string.ascii_uppercase + string.digits
    return ''.join(random.choices(caracteres, k=6))