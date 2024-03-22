# raise - lançando exceções (erros)
# 

def dividir_por_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True

def verificar_tipo(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )

def divide(n, d):
    verificar_tipo(n)
    verificar_tipo(d)
    dividir_por_zero(d)
    return n / d

print(divide(8,0))
