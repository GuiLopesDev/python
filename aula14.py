a = 'A'
b = 'B'
c = 1.1
formato1 = 'a={} b={} c={:.2f}'.format(a, b, c) # Dessa forma é levado em consideração a ordem do format, sempre seguindo no momento de usar os valores de parametro

formato2 = 'b={1} a={0} c={2:.2f}'.format(a, b, c) # Dessa forma é levado em consideração o indice assim podendo ser invertido a sequencia de valores

formato3 = 'c={nome3:.2f} b={nome2} a={nome1}'.format(
    nome1=a, 
    nome2=b, 
    nome3=c) # Nomeando os parametros todos depois dele tem a obrigação de serem nomeados, caso não seja apresenta erro. Uso deles fica livre, sem estar preso a uma ordem.

print(formato1)
print(formato2)
print(formato3)