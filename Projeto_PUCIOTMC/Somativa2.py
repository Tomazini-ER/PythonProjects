import paho.mqtt.client as mqtt
import time
from hal import temperatura1, temperatura2, aquecedor, aquecedor2, mensagem, mensagem2
from definicoes import client_id, user, password, server, port, client_id2, user2, password2, server2, port2
##import RPi.GPIO as GPIO -> nem mesmo foi reconhecido pela IDE
##import Adafruit_DHT funcionou
## Variáveis na aba definições
## funções na aba hal

import random



## conexão dispositivo 1

client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

## conexão dispositivo 2

client2 = mqtt.Client(client_id2)
client2.username_pw_set(user2, password2)
client2.connect(server2, port2)

## termostáto 1
client.on_message = mensagem
client.subscribe(f'v1/{user}/things/{client_id}/cmd/2')
client.loop_start()

## termostáto 2
client2.on_message = mensagem2
client2.subscribe (f'v1/{user}/things/{client_id}/cmd/3')
client2.loop_start()


while True:
    client.publish (f'v1/{user}/things/{client_id}/data/0', temperatura1())
    client2.publish (f'v1/{user2}/things/{client_id2}/data/1', temperatura2())
    time.sleep(10)


#client.disconnect()
#client2.disconnect()