'''
Crie funções que duplicam, triplicam e quadruplicam o
número recebido como parâmetro.
'''
numero = int(input('Qual numero deseja ver os multiplos? '))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

for mult in range(1,11):
    calculo = criar_multiplicador(mult)
    print(calculo(numero))
