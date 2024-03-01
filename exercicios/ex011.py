"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301

Multiplicar o resultado anterior por 10
301 * 10 = 3010

Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7

Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = '746.824.890-70'
numeros = []
numeros_multiplicados = []
contador = 10
somatoria = 0

# Separando os números para verificar
for num in cpf:
    try:
        numeros.append(int(num))
    except:
        continue

# Primeira etapa de verificação
for num_mult in numeros:
    numeros_multiplicados.append(num_mult*contador)
    # Segunda etapa de verificação
    somatoria += numeros_multiplicados[-1]

    contador += -1
    if contador < 2:
        break

primeiro_num = (somatoria*10)%11

# Terceira etapa de verificação
etapa3 = primeiro_num > 9
verificacao = 'Primeiro digito é 0' if etapa3 else f'Primeiro digito é {primeiro_num}'