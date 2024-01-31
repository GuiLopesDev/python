'''
 Os operadores são calculados na seguinte ordem:
    1. ( N + N )
    2. **
    3. * / // %
    4. + -
'''
conta = 1 + 1 ** 5 + 5 
conta_correta = (1 + 1) ** (5 + 5)

print(conta)
print(conta_correta)