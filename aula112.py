# Problema dos parâmetros mutáveis em funções python

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)

cliente2 = adiciona_clientes('Maria')
adiciona_clientes('Joana', cliente2)

cliente3 = adiciona_clientes('Jose')
adiciona_clientes('Jose', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)