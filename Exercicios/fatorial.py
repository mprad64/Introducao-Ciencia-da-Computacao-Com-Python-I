from socket import NI_NUMERICHOST


n = int(input("Digite o valor de n>: "))

resultado = 1
count = 1

while count <= n:
    resultado = resultado * count
    count = count + 1
print(resultado)
