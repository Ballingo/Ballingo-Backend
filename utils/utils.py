import random

def generate_recovery_code():
    code = ''.join(random.choices('0123456789', k=5))
    return code