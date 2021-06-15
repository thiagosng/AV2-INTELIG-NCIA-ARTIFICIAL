import random
import numpy as np
import math


def randomIdeais():
    return np.random.random((10))


def randomPesos():
    Pesos = []
    i = 0
    while i < 10:
        Pesos.append(np.random.random((10)))
        i += 1
    return Pesos


def randomEntradas():
    return np.random.random((10))


def custo(obtidos, ideais):
    custoTotal = 0
    i = 0
    for obtido in obtidos:
        custoTotal += math.pow((obtido + ideais[i]), 2)
        i += 1
    custoTotal = round(custoTotal, 2)

    return custoTotal


def soma(entradas, pesos):
    soma = 0
    i = 0
    for entrada in entradas:
        soma += entrada * pesos[i]
        i += 1
    return soma


# Main

def main():
    # calculando o custo inicial
    Pesos = randomPesos()
    entradas = randomEntradas()
    ideais = randomIdeais()

    obtidos = []

    for pesos in Pesos:
        obtidos.append(soma(entradas, pesos))

    custoIdeal = custo(obtidos, ideais)

    print("O valor do custo é: ", custoIdeal)


main()