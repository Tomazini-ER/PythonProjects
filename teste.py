#input().split() é uma forma muito interessante de inserir valores com espaço como se fosse um append
entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

# TODO: Calcule o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais no espaço #em branco abaixo:
ICM = distancia/(diametro1 + diametro2)
print (f' o ICM é {ICM:.2f}')

# ou usar round
print (round(ICM, 2))
print ('%.2f'%(ICM)) # essa a forma que queriam

# exemplo 2
valores = input().split()
tempo = int(valores[0])
velocidade = int(valores[1])
rendimento = 12

# TODO:  Calcule quantidade de litros necessária para realizar a viagem e imprima com TRÊS dígitos após o ponto decimal
combustivel = (velocidade*tempo)/rendimento
print ('%.3f'%(combustivel))