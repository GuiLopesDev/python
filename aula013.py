'''
Exercicio de calculo de IMC com variaveis
'''

nome = 'Guilherme'
altura = 1.79
peso = 125
imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura} de altura'
linha_2 = f'pesa, {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)