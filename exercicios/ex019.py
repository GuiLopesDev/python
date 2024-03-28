# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
lista_cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_estados = ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def zipper(lista1, lista2):
#     intervalo_maximo = (min(len(lista1)), len(lista2))
#     return [
#         (lista1[i], lista2[i]) for i in range(intervalo_maximo)
#     ]

# print(zipper(lista_cidades, lista_estados))

print(list(zip(lista_cidades, lista_estados)))

from itertools import zip_longest

print(list(zip_longest(lista_estados, lista_cidades, fillvalue='Sem cidade')))