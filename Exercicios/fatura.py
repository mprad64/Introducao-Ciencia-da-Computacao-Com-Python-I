cliente = str(input("Digite o nome do cliente: "))
diaVencimento = int(input("Digite o dia do vencimento: "))
mesVencimento = str(input("Digite o mês de vencimento "))
valorFatura = str(input("Digite o valor da fatura: "))

print(f"Olá, {cliente}")
print(f"A sua fatura com vencimento em {diaVencimento} de {mesVencimento} no valor de R$ {valorFatura} está fechada.")
