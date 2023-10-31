def operacoes(oper, num1, num2):
    if oper == 1:
        soma = num1 + num2
        return f'O Resultado da soma é:  {soma}'
    elif oper == 2:
        if num1 > num2:
            subtracao = num1 - num2
        else:
            subtracao = num2 - num1
        return f'O Resultado da subtração é:  {subtracao}'
    elif oper == 3:
        multiplicacao = num1 * num2
        return f'O Resultado da multiplicação é:  {multiplicacao}'
    elif oper == 4:
        if num1 == 0 or num2 == 0:
            divisao = "Divisão por 0 não existe"
        else:
            if num1 > num2:
                divisao = num1 / num2
            else:
                divisao = num2 / num1

        return f'O Resultado da divisão é:  {divisao}'
    else:
        return "Operação inexistente na função! "


while True:
    operacao = int(input("""Informe qual operação deseja efetuar:
                         
1- Soma
2- Subtração ( nessa função sempre subtrairá o maior pelo menor)
3- Multiplicação
4- Divisão ( nessa função sempre dividirá o maior pelo menor)
0- Sair:   """))
    if operacao == 0:
        break
    print()
    numero1 = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))
    print()
    print(operacoes(operacao, numero1, numero2))
    print()
    
