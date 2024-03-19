# Introdução às Generator functions em Python

def generator(n=0, maximun=10):
    while True:
        yield n
        n += 1

        if n >= maximun:
            return


gen = generator()

for n in gen:
    print(n)