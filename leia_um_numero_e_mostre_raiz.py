num = int(input("Digite um número: "))
if num < 0:
    print("Você digitou um número negativo.")
else:
    print(f"A raiz quadrada de {num} é {num ** (1/2):.2f}")