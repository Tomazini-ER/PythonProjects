while True:
    print('Iniciando: ')
    print('Bem vindo a calculadora Py! ')
    print('')
    print('')
    print('')
    print('A partir daqui, serão pedidos numeros e operadores para os calculos...')
    print('')
    print('')
    
    numero1 = input('Digite um numero: ')
    numero2 = input('Digite outro numero: ')
    operador = input('Digite o operador: ')
    numeros_validos = None
    

    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_validos= True

    except Exception as error:
        numeros_validos = None

    

    if numeros_validos is None:
        print(' algum dos numeros digitados não é valido: ')
        continue

    operadores_permitidos = '+-*/%//**'

    if operador not in operadores_permitidos:
        print (' operador não é válido! ')    
        continue

    if len(operador) > 3:  
        print (' operador não é válido!, entre apenas com operadores de até 2 digitos:  ')    
        continue
    ################################################################

    if operador == '+':
        soma = num1_float + num2_float
        print (f'operação de soma entre, {num1_float}, e {num2_float}: ')
        print ('')
        print (' o resultado da operação é:   ')
        print (soma)

    elif operador == '-':
        print (f'operação de subtração entre, {num1_float}, e {num2_float}: ')
        print ('')
        subtração = num1_float - num2_float
        print (' o resultado da operação é:   ')
        print (subtração)

    elif operador == '*':
        print (f'operação de multiplicação entre, {num1_float}, e {num2_float}: ')
        print ('')
        multiplicacao = num1_float * num2_float
        print (' o resultado da operação é:   ')
        print (multiplicacao)

    elif operador == '/':
        print (f'operação de divisão entre, {num1_float}, e {num2_float}: ')
        print ('')
        divisao = num1_float / num2_float
        print (' o resultado da operação é:   ')
        print (divisao)

    elif operador == '**':
        print (f'operação de potenciação entre, {num1_float}, e {num2_float}: ')
        print ('')
        potenciacao = num1_float ** num2_float
        print (' o resultado da operação é:   ')
        print (potenciacao)
    
    elif operador == '//':
        print (f'operação de radiciação entre, {num1_float}, e {num2_float}: ')
        print ('')
        radiciacao = num1_float // num2_float
        print (' o resultado da operação é:   ')
        print (radiciacao)
    
    elif operador == '%':
        print (f'operação de resto entre, {num1_float}, e {num2_float}: ')
        print ('')
        resto = num1_float % num2_float
        print (' o resultado da operação é:   ')
        print (resto)

    sair = input('Digite [S]air').lower().startswith('s')
    if sair is True:
        break