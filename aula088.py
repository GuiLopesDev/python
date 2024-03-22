import importlib

import aula088_m

print(aula088_m.variavel)

for i in range(10):
    importlib.reload(aula088_m)
    print(i)