primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

num1 = int(primeiro_valor)
num2 = int(segundo_valor)

if num1 >= num2:
    print(f'{num1} é maior que {num2}!')
else:
    print(f'{num2} é maior que {num1}!')