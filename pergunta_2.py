'''
Desenvolva uma outra função que implementa o a ordenação 
utilizando o Quick Sort e meça o tempo levado para fazer a ordenação.

Aluno: ATTILA SAMUELL NUNES TABORY 
'''

def quickSort(lista):
   ajudandoQuickSort(lista,0,len(lista)-1)

def ajudandoQuickSort(lista,primeiro,ultimo):
   if primeiro<ultimo:

       divisaoPonto = partindo(lista,primeiro,ultimo)

       ajudandoQuickSort(lista,primeiro,divisaoPonto-1)
       ajudandoQuickSort(lista,divisaoPonto+1,ultimo)


def partindo(lista,primeiro,ultimo):
   valorPivor = lista[primeiro]

   esquerda = primeiro+1
   direita = ultimo

   done = False
   while not done:

       while esquerda <= direita and lista[esquerda] <= valorPivor:
           esquerda = esquerda + 1

       while lista[direita] >= valorPivor and direita >= esquerda:
           direita = direita -1

       if direita < esquerda:
           done = True
       else:
           temp = lista[esquerda]
           lista[esquerda] = lista[direita]
           lista[direita] = temp

   temp = lista[primeiro]
   lista[primeiro] = lista[direita]
   lista[direita] = temp


   return direita

lista = [64,36,103,27,86,44,48,65,28]
quickSort(lista)
print(lista)