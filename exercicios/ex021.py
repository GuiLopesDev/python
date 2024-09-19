'''
Exercício - Lista de tarefas com desfazer e refazer
   - Listar
   - Desfazer a ultima operação (10, 9, 8, 7 ...)
   - Refazer (7, 8, 9, 10)
'''
def lista_comandos(comando):
    if comando == 'listar':
        print(*TodoList)
    elif comando == 'desfazer':
        desfazerList.append(TodoList(-1))
        TodoList.pop()
        print(*TodoList)
    elif comando == 'refazer':
        TodoList.append(desfazerList(-1))
        desfazerList.pop()
        print(*TodoList)
    else:
        TodoList.append(comando)
        print(*TodoList)
    

TodoList =[
        'TAREFAS:',
        ]
desfazerList =[]

while len(TodoList) < 10:
    print('Comandos: listar, desfazer, refazer')
    comando = input('Digite uma tarefa ou comando: ')
    lista_comandos(comando)
