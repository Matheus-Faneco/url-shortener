import random
import string


def generate_code():
    caracteres = string.ascii_uppercase + string.digits
    return ''.join(random.choices(caracteres, k=6))