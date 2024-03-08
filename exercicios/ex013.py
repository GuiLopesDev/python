'''
Exercícios com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável.
'''
def multiplicacao(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

conta = multiplicacao(10, 2, 3, 4)
print(conta)

# Crie uma função que retorna se um número é par ou impar

def par_impar(x):
    multiplo_de_dois = x % 2 == 0

    if multiplo_de_dois:
        return f'{x} é par'
    return f'{x} é ímpar'

print(par_impar(1))
print(par_impar(20))
print(par_impar(35))