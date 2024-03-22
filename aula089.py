import aula089_package
print(aula089_package.modulo.soma_modulo(1, 2))


from aula089_package.modulo import soma_modulo
print(soma_modulo(1, 2))

from aula089_package import modulo
print(modulo.soma_modulo(1, 2))