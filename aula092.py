'''
Funções decoradoras e decoradores
Decorar = Adicionar / Remover / Restringir / Alterar
Funções decoradoras são funções que decoram outras funções
Decoradores são usado para fazer o Python
usar as funções decoradas em outras funções
'''

def criar_funcao(func):
    def funcao_interna(*args, **kwargs):
        print('Vou te decorar')

        for arg in args:
            e_string(arg)
        
        resultado = func(*args, **kwargs)
        print('Ok, agora você foi decorada')
        print(f'O seu resultado foi {resultado}')

        return resultado
    
    return funcao_interna

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Parametro deve ser uma string')

def inverte_string(string):
    return string[::-1]

inverte_string_checando_type = criar_funcao(inverte_string)
invertida = inverte_string_checando_type('123')
print(invertida)