import random

def cumprimento(texto):
    return f"Olá, {texto}"

nome = "Vitória Moro"

print(cumprimento(nome))

def sorteio():
    numeros = [random.randint(1,100) for _ in range(7)]
    media = sum(numeros) / len(numeros)
    return f"Os números sorteados são {numeros} e a sua média é {media:.2f}"

print(sorteio())