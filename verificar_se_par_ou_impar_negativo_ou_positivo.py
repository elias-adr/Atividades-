num = int(input("Digite um número positivo ou negativo: "))
if num < 0 and num % 2 ==0:
    print("Seu número é par negativo.")
elif num < 0 and num % 2 ==1:
    print("Seu número é ímpar negativo.")
elif num % 2 ==0:
    print("Seu número é par positivo.")
else:
    print("Seu número é ímpar positivo.")