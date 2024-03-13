# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set()  # vazio
s1 = {'Gui', 1, 2, 3}  # com dados
print(s1)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
s1 = {1,2,3,4,4,4,4}
print(s1)

# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Gui')
s1.update(('Olá mundo',1,2,3,4,4,4,4,4,4,4,4))
#s1.clear()
s1.discard('Olá mundo')
print(s1)

# Operadores úteis:
s1 = {1,2,3}
s2 = {2,3,4}

# união | união (union) - Une
s3 = s1 | s2
print(s3)

# intersecção & (intersection) - Itens presentes em ambos
s4 = s1 & s2
print(s4)

# diferença - Itens presentes apenas no set da esquerda
s5 = s2 - s1
print(s5)

# diferença simétrica ^ - Itens que não estão em ambos
s6 = s1 ^ s2
print(s6)