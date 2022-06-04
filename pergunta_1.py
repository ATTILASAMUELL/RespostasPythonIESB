'''
Desenvolva um programa em python que gere uma lista com 50 números aleatórios. A seguir, 
elabore uma função que implementa a ordenação utilizando Buble Sort e meça o tempo que
levou para realizar a ordenação da lista criada anteriormente.
Aluno: ATTILA SAMUELL NUNES TABORY 
'''

import time
def bubleSort (lista):
  
  elementos = len(lista)-1
  ordenado = False
  while not ordenado:
    
    ordenado = True
    for i in range(elementos):
      if lista[i] > lista[i+1]:
        lista[i], lista[i+1] = lista[i+1],lista[i]
        ordenado = False        
        print(lista)
  return lista


inicio = time.time()
bubleSort ([5, 1, 4, 2])
fim = time.time()
print('Tempo:')
print(fim - inicio)