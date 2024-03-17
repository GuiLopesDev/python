'''
Valores Truthy e Falsy, tipos mutáveis e imutáveis
Mutáveis [] {} set()
Imutáveis () '' 0 1.1 None False range(0, 10)
'''

lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False 
intervalo = range(0)

def falsy(valor):
    return 'Falsy' if not valor else 'truthy'