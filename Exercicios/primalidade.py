""" Exercício 1
Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo". """

num = int(input("Digite um número inteiro: "))
i = 2
primo = True
if num % i == 0:
    print("não primo")
    i = i + 11

if primo:
    print("primo")
