"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4, 'b']
lista_soma = []

def somar(l1, l2):
    indices = min(len(l1), len(l2))
    for i in range (indices):
        if not isinstance(l1[i], (int, float)):
            print(f'Valor de indice {i} na primeira lista não é um número')
            break

        if not isinstance(l2[i], (int, float)):
            print(f'Valor de indice {i} na segunda lista não é um número')
            break

        else:        
            lista_soma.append(l1[i] + l2[i])

somar(lista_a, lista_b)
print(lista_soma)