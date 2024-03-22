# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print(1)
    8/0
except ZeroDivisionError:
    print('Dividiu zero')
else:
    print('Não deu erro')
finally:
    print(2)
    