'''
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa(shallow copy)
get - obtém uma chave
pop - Apaga um item com chave especificada(del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
'''
pessoa ={
    'nome': 'Guilherme',
    'sobrenome': 'Oliveira',
}

# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))
# pessoa.setdefault('idade', 0)

# Shallow copy -> Copia rasa, copia somente os valores imutaveis

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0,1,2]
# }

# d2 = d1.copy()
# d2['c1'] = 1000
# d2['l1'][1] = 1596

# print(d1)
# print(d2)

#Deepcopy -> copia tudo, imutaveis e mutaveis

# import copy

# d3 = copy.deepcopy(d1)
# d3['l1'][1] = 444

# print (d3)

# print(pessoa.get('nome', 'Não existe'))

# ultima_chave = pessoa.popitem()
# print(ultima_chave)
# print(pessoa)

pessoa.update({
    'nome': 'novo valor',
    'idade': 25    
})

pessoa.update(nome = 'novo valor', idade = 30)

tupla = (('nome', 'novo valor'),('idade', 30))
pessoa.update(tupla)