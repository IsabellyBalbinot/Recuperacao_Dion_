
num1 = int(input("Digite o primeiro número: "))


num2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação (+, -, *, /): ")


if operacao == "+":
    resultado = num1 + num2
    print("Resultado:", resultado)

elif operacao == "-":
    resultado = num1 - num2
    print("Resultado:", resultado)

elif operacao == "*":
    resultado = num1 * num2
    print("Resultado:", resultado)

elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)

    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")