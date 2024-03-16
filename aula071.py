# Empacotamento e desempacotamento de dicionários

# a, b = 1, 2
# a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# primeira_key, segunda_key = pessoa
# print(primeira_key, segunda_key)

# primeiro_valor, segundo_valor = pessoa.values()
# print(primeiro_valor, segundo_valor)

# primeiro_item_mais_valor, segundo_item_mais_valor = pessoa.items()
# print(primeiro_item_mais_valor, segundo_item_mais_valor)

# (a1, a2), b = pessoa.items()
# print(a1, a2)

# for chave, valor in pessoa.items:
#     print(valor)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

# args e kwargs
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

nome = input('Qual seu nome: ')
idade = input('Qual sua idade: ')

mostro_argumentos_nomeados(nome=nome, idade=idade)
mostro_argumentos_nomeados(**pessoa_completa)