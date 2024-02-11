'''
Iterando strings com while
'''

nome = 'Guilherme'
indice = 0
novo_nome = ''

while indice < len(nome):
    novo_nome += f'*{nome[indice]}'
    indice += 1
    if indice == len(nome):
        novo_nome += ('*')

print(novo_nome)
    