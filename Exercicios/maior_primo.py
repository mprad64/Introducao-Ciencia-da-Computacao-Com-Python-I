""" Exercício 2 - Primos
Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função """


def maior_primo (x):
    if x >= 2:
        contador = 1
        while contador <= x:
            