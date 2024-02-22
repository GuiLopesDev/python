'''
Faça uma lista de compras usando lista
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista.
'''

lista_compras = []

while True:
    
    print('Selecione uma opção')
    opcao_selecionada = input('[i]nserir [a]pagar [l]istar: ')
    
    # Inserir produtos

    if opcao_selecionada == 'i':
        produto_adicionado = input('Insira o produto desejado: ')
        lista_compras.append(produto_adicionado)
    
    # Apagar produtos

    elif opcao_selecionada == 'a':
        indice_apagar = input('Escolha o índice para apagar: ')
        try:    
            lista_compras.pop(int(indice_apagar))
        except:
            print('Não foi possível apagar este índice')

    # Listar produtos

    elif opcao_selecionada == 'l':
        for indice, produto in enumerate(lista_compras):
            print(indice, produto)
    
    # Opção selecionada inválida

    else:
        print('Essa opção não é válida')