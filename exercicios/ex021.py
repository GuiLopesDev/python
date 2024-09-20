'''
Exercício - Lista de tarefas com desfazer e refazer
   - Listar
   - Desfazer a ultima operação (10, 9, 8, 7 ...)
   - Refazer (7, 8, 9, 10)
'''
toDoList =[]
desfazerList =[]

def listar(toDoList):
    print()
    if not toDoList:
        print('Nenhuma tarefa para listar')
        return
    
    print('Tarefas: ')
    for tarefa in toDoList:
        print(f'\t{tarefa}')

def desfazer(toDoList, desfazerList):
    print()
    if not toDoList:
        print('Nenhuma tarefa para desfazer')
        return
    tarefa = toDoList.pop()
    desfazerList.append(tarefa)

def refazer(toDoList, desfazerList):
    print()
    if not toDoList:
        print('Nenhuma tarefa para refazer')
        return
    tarefa = desfazerList.pop()
    toDoList.append(tarefa)

def adicionar(toDoList, comando):
    print()
    tarefa = comando.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    toDoList.append(tarefa)
    listar(toDoList)

while True:
    print('Comandos: listar, desfazer, refazer')
    comando = input('Digite uma tarefa ou comando: ')
    
    if comando == 'listar':
        listar(toDoList)
    elif comando == 'desfazer':
        desfazer(toDoList, desfazerList)
    elif comando == 'refazer':
        refazer(toDoList, desfazerList)
    else:
        adicionar(toDoList, comando)
