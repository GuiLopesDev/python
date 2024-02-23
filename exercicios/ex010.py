'''
Faça uma lista de compras usando lista
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista.
'''
import os # Usado para limpar o terminal, facilitando a visualização do usuário 
lista_compras = []

while True:
    
    print('Selecione uma opção')
    opcao_selecionada = input('[i]nserir [a]pagar [l]istar: ')
    
    # Inserir produtos

    if opcao_selecionada == 'i':

        os.system('clear')

        produto_adicionado = input('Insira o produto desejado: ')
        lista_compras.append(produto_adicionado)
    
    # Apagar produtos

    elif opcao_selecionada == 'a':
        
        indice_apagar = input('Escolha o índice para apagar: ')

        # Tratativa dos erros possíveis

        try:    
            lista_compras.pop(int(indice_apagar))
        except TypeError:
            print('Por favor indique o indice usando número inteiro')
        except IndexError:
            print('Índice inexistente')
        except Exception:
            print('Erro desconhecido')

        os.system('clear')

    # Listar produtos

    elif opcao_selecionada == 'l':

        os.system('clear')

        # Tratativa de tentativa para listagem vazia

        if len(lista_compras) == 0:
            print('Sua lista está vazia')
            continue

        for indice, produto in enumerate(lista_compras):
            print(indice, produto)
    
    # Opção selecionada inválida

    else:
        print('Essa opção não é válida')