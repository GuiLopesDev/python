# isinstance - para saber se objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Gui'}
]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item)

    elif isinstance(item, str):
        print(item.upper())

    elif isinstance(item, (int, float)):
        print(item, item *2)

    else:
        print('Outro tipo', item)
