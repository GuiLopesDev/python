# Manipulando chaves e valores em dicionários

pessoa = {}

pessoa['nome'] = 'Guilherme'
pessoa['sobrenome'] = 'Oliveira'
print(pessoa)

del pessoa['sobrenome']

if pessoa.get('sobrenome') is None:
    print('Sobrenome não exite')
else:
    print(pessoa ['sobrenome'])