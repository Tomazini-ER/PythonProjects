palavra_secreta = 'pernilongo'
letras_acertadas = ''
numero_tentativas = 0
while True:
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra: ')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        print('você digitou uma letra correta! ')
        print (letras_acertadas)

    elif letra_digitada not in palavra_secreta:
        print ('Você errou, perdeu uma tentativa. ')
        numero_tentativas += 1
        print ('você tem mais: ', 5 - numero_tentativas, ' chances ')

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
        
    print ("A palavra formada é: ", palavra_formada)
    
    if palavra_formada == palavra_secreta:
        print (' você ganhou')
        print ('A palavra secreta era: ', palavra_secreta)

    if numero_tentativas >= 5:
        print ('Você perdeu')
        break
    
    
    
    
