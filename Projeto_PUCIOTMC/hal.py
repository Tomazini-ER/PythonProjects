import random

def temperatura1():
    temperaturaa = 10
    temperatura1 = temperaturaa + random.randrange(-1, 2)
     ## Adafuirt_DHT.read_retry(Adafruit_DHT.DHT11, 4) caso estivesse ligado
    return temperatura1

def temperatura2():
    temperaturab = 15
    temperatura2 = temperaturab + random.randrange(1, 3)
     ## Adafuirt_DHT.read_retry(Adafruit_DHT.DHT11, 4) caso estivesse ligado
    return temperatura2

def aquecedor (estado:str):
    if estado == 'on':
        print ('ligado')

    else:
        print ('desligado')

def aquecedor2 (estado:str):
    if estado == 'on':
        print ('ligado')

    else:
        print ('desligado')

def mensagem(client, userdata, msg):
    vetor = msg.payload.decode().split(',')
    aquecedor('on' if vetor[1] == '1' else 'off')
    client.publish (f'v1/{user}/things/{client_id}/response', f'ok, {vetor[0]}')
    print (vetor)

def mensagem2(client2, user2data, msg2):
    vetor2 = msg2.payload.decode().split(',')
    aquecedor2('on' if vetor[1] == '1' else 'off')
    client2.publish (f'v1/{user2}/things/{client_id2}/response', f'ok, {vetor2[0]}')
    print (vetor2)