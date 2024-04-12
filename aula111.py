import json

pessoa = {
    'nome': 'Guilherme',
    'sobrenome': 'Oliveira',
    'nome': [
        {'rua': 'R1', 'numero': 35},
        {'rua': 'R2', 'numero': 32}
    ],
    'altura': 1.8,
    'numeros_preferidos': (2,4,7),
    'dev': True,
    'nada': None,
}

with open('aula111.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

with open('aula111.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)