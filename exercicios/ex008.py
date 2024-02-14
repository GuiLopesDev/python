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
contador = 0
palavra_secreta = 'Perfume'
palavra_formatada = '*******'

while True:

    letra_inserida = input('Digite uma letra: ')

    # Verificação de entrada de dados
    if len(letra_inserida) != 1 or not letra_inserida.isnumeric:
        print('Digite apenas uma letra')
        continue

    # Verificação se a letra inserida está na palavra
    for letra in palavra_secreta:

        print(letra)

        if letra in palavra_secreta[contador]:
            print(palavra_secreta[contador])

        contador += 1

    print('Palavra formatada: ',palavra_formatada)
    if '*' not in palavra_formatada:
        break
