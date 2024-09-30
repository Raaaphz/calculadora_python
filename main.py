continuar = 1

while continuar == 1:
    firstnum = float(input('Insira o primeiro número: '))
    secnum = float(input('Insira o segundo número: '))
    
    print('Digite o número que corresponde à operação da conta que quer realizar:')
    print('1. Somar // 2. Subtrair // 3. Multiplicar // 4. Dividir')
    
    sinal = int(input())
    resultado = float(0)

    if sinal == 1:
        resultado = firstnum + secnum
        print(f'Resultado da soma: {resultado}')
    elif sinal == 2:
        resultado = firstnum - secnum
        print(f'Resultado da subtração: {resultado}')
    elif sinal == 3:
        resultado = firstnum * secnum
        print(f'Resultado da multiplicação: {resultado}')
    elif sinal == 4:
        if secnum != 0:
            resultado = firstnum / secnum
            print(f'Resultado da divisão: {resultado}')
        else:
            print('Erro: Não é possível dividir por zero.')
    else:
        print('O número digitado não é um sinal válido.')
    
    continuar = int(input('Deseja continuar? (1 para sim, 0 para não): '))