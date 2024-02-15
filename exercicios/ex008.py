"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

palavra_secreta = 'Perfume'
letras_corretas = ''
tentativas = 0

while True:

    letra_inserida = input('Digite uma letra: ')
    tentativas += 1

    # Verificação de entrada de dados
    if len(letra_inserida) != 1 or not letra_inserida.isnumeric:
        print('Digite apenas uma letra')
        continue

    # Verificação se a letra inserida está na palavra
    
    if letra_inserida in palavra_secreta:
        letras_corretas += letra_inserida

    palavra_formatada = ''
    
    for letra in palavra_secreta:
        if letra in letras_corretas:
            palavra_formatada += letra
        else:
            palavra_formatada += '*'
    print('Palavra formada:', palavra_formatada)

    # Verificação se a palavra está completa e correta

    if palavra_formatada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas: ', tentativas)
        letras_corretas = ''
        tentativas = 0
