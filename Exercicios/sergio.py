# Lê o número de notas
n = int(input("Insira o número de notas: "))

# Inicializa a variável de soma com 0
soma = 0

# Lê as notas e as adiciona à soma
for i in range(n):
  nota = float(input("Insira a nota: "))
  soma += nota

# Calcula a média aritmética
media = soma / n

# Imprime o resultado
print("A média aritmética é", media)
