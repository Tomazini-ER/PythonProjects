## ESTEVAN RAFAEL TOMAZINI
## PONTIFICIA UNIVERSIDADE CATOLICA DO PARANÁ
## BIGDATA E INTELIGÊNCIA ANALÍTICA
## DISCIPLINA DE RACIOCÍNIO COMPUTACIONAL
## PROFESSOR LUCAS EMANUEL SILVA E OLIVEIRA
## ENTREGA DO ZOMBIE DICE SEMANA 8


##INICIO

## Gerar lista de jogadores:

import random

print ("ZOMBIE DICE (Protótipo Semana 8) ")
print ("BEM VINDO AO ZOMBIE DICE!")

numJogadores = 0
while numJogadores < 2:
	print ("Qual é o numero de jogadores? ")
	numJogadores = int (input ())

	if numJogadores < 2 :
		print ("AVISO: Você precisa de pelo menos 2 jogadores!")
	##FIMSE

##FIMENQUANTO


listaJogadores = []

for i in range (numJogadores):
	nome = input("Nome do jogador " + str(i + 1) + ": ")
	listaJogadores.append(nome)

print(listaJogadores)
print("Iniciando Zombie dice..")

##FIMPARA

## gerar conjunto de dados possíveis

dadoVerde = "CPCTPC"
dadoAmarelo = "TPCTPC"
dadoVermelho = "TPTCPT"
listaDados = [dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoVermelho, dadoVermelho, dadoVermelho]
print ("INICIANDO O JOGO...")

## Turnos do jogo e faces selecionadas


jogadorAtual = 0
dadosSorteados = []
tiros = 0
cerebros = 0
passos = 0

while True:
	print ("TURNO DO JOGADOR ", listaJogadores[jogadorAtual])
	for i in range (3):
		numSorteado = random.randint (0, 12)
		dadoSorteado = listaDados[numSorteado]

		if dadoSorteado == 'CPCTPC':
			corDado = 'VERDE'
		elif dadoSorteado == 'TPCTPC':
			corDado = 'AMARELO'
		else:
			corDado = 'VERMELHO'
		##FIMSE

		print ("Dado sorteado: ", corDado)
		dadosSorteados.append (dadoSorteado)

	##FIMPARA


	print ("As faces sorteadas foram: ", dadosSorteados)

	for dadoSorteado in dadosSorteados:
		numFaceDado = random.randint(0, 5)
		if dadoSorteado[numFaceDado] == "C" :
			print ("- CÉREBRO (você comeu um cérebro)")
			cerebros = cerebros + 1

		elif dadoSorteado[numFaceDado] == "T" :
			print ("- TIRO (você levou um tiro)")
			tiros = tiros + 1

		else:
			print ("- PASSOS (uma vítima escapou)")
			passos = passos + 1
		##FIMSE

	##FIMPARA

## turnos e continuar jogando
## não consegui trocar o jogador

	print ("SCORE ATUAL: ")
	print ("CÉREBROS: ", cerebros)
	print ("TIROS: ", tiros)
	print("AVISO: Você deseja continuar jogando dados? (s = sim / n = não / d = desistir)")
	continuarTurno = str (input())

	if continuarTurno.lower() == "s":
		print("continuando com a proxima rodada do jogador ", jogadorAtual)
		dadosSorteados = []
		if tiros >= 3:
			print(jogadorAtual, "Tomou três balaços, perdeu a vez!")
			jogadorAtual = jogadorAtual + 1
			dadosSorteados = []
			tiros = 0
			cerebros = 0
			passos = 0
			print("Trocando de jogador para ", jogadorAtual)
			if jogadorAtual == len(listaJogadores):
				jogadorAtual = 0
				continue
		elif cerebros >= 13:
			print(jogadorAtual, ' Ganhou! parabéns!')
			break
		else:
			continue


	elif continuarTurno.lower() == "n":
		jogadorAtual = jogadorAtual + 1
		dadosSorteados = []
		tiros = 0
		cerebros = 0
		passos = 0
		print("Trocando de jogador para ", jogadorAtual)
		if jogadorAtual == len (listaJogadores):
			jogadorAtual = 0
			continue

	elif continuarTurno.lower () == "d" :
		print ("Encerrando Zombie Dice, obrigado por jogar!")
		break


## condicional para a vitória e passada de turno

	##FIMIF


##FIMelse

##FIMwhile
##FIM