'''
Pode ser alterado o parametro de separação usando sep='', para que mude a divisão default do print que seria um espaço simples.
Usando o parametro end='', se torna possivel mudar o final de um print, mudando o default que é a quebra de linha: \r\n -> CRLF (Windows), \n -> LF (Linux, ios)
'''
print(12, 34, sep=' eita ', end='#\n') 
print(12, 34, sep='-') 
print(12, 34, sep=' oia ') 