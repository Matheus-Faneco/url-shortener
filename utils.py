import random
import string


def gerar_codigo_url_encurtada():
    caracteres = string.ascii_uppercase + string.digits
    return ''.join(random.choices(caracteres, k=6))