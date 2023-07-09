lista = ['Jó','Mó','Có','Dó', 'Tó']
lista2 = enumerate(lista) # retorna locais na moméria onde objeto da lista está 
print (lista2)

for item in lista2:
    print(item)  # observem que retorna tupla, que permite desempacotamento

for item in enumerate(lista):
    indice, nome = item
    print (indice, nome)  # Que também pode ser simplificado em 1 linha de código

for item in enumerate(lista):
    print('For da tupla')
    for valor in item:
        print (f'\t{valor}')  # iterando os elementos da tupla, espaçamento em TAB