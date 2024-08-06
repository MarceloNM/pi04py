# MarceloNM 2403 final
'''IEFP-PI04-10793-Phyton- T1 - Euromilhões
Para entrega a 4 de março de 2024 às 23:59
10793

Instruções
Nome do projeto: "Euromilhões"
Pedir ao utilizador 5 números e 2 estrelas
Gerar os números e estrelas do Euromilhões de forma aleatória
Mostrar o resultado pela ordem de saída
Mostrar o resultado por ordem crescente
Verificar se o utilizador acertou em algum número ou em alguma estrela
Jogar 100 semanas seguidas com a mesma aposta e mostrar em que semanas
 pelo menos acertou um número ou uma estrela
Boa apresentação do código
Com comentários'''

import random


''' Inventa lista de números aleatórios num intervalo 
'min'-limite inferior, 'max'-limite superior, 'comp'-  '''
def rnd_int_lista(min : int, max : int, comp : int ):
    n = 0
    numeros : int = []      
    while n < comp:   # ciclo de preenchimento da lista
        r = random.randrange(min, max+1)
        k = 0 
        unico = True
        while unico and k < n:   # ciclo de validação de número
            if r == numeros[k]:  # é repetido 
                unico = False      # termina as comparações
            #    print("repetido")  # print para teste
            #    print(r)
            else:
                k += 1
        if unico:                   # se é único pode ser guardado e passar ao seguinte
            numeros.append(r)
            n += 1
    numeros.sort()
    return numeros
# fim da função rnd_int_lista

''' Devolve número de elementos comuns a duas listas '''
def compara_listas(lista1 : list, lista2 : list):
    n = 0
    for i in lista2:
        if i in lista1:
            n += 1
            # print(n)     # para teste
    return n
# fim da função compara_listas

''' Lê do user lista de comprimento comp com inteiros entre min e max  '''
def ler_int_lista(min : int , max : int , comp : int):
    n = 0 
    numeros : int = []
    print("Escolha ", comp, " números entre ", min, " e ", max, ":")
    while n < comp:
        num : int  = 0
        num = int(input(" => "))
        if num in range(min, max + 1):
            if num in numeros:
                print("Número repetido!")
            else:
                numeros.append(num)
                # print(n + 1, " => ", num)
                n += 1
        else:
            print("Número fora do intervalo [", min, ", ", max, "]")
    numeros.sort()
    return numeros
# fim da função ler_int_lista




# main 

MAXSEMANAS : int = 105   # projeto com 100 semanas (105000 semanas são 2000 anos)

# Nomes dos prémios
lista_premios = ["Décimo terceiro", "Décimo segundo", "Décimo primeiro", "Décimo", "Nono", "Oitavo", "Sétimo", "Sexto", "Quinto", "Quarto", "Terceiro", "Segundo", "Primeiro"]
# 'códigos' para o dicionário
# 2+0, 2+1, 1+2, 3+0, 3+1, 2+2, 4+0, 3+2, 4+1, 4+2, 5+0, 5+1, 5+2
dict_premios = {20: 0, 21: 0, 12: 0, 30: 0, 31: 0, 22: 0, 40: 0, 32: 0, 41: 0, 42: 0, 50: 0, 51: 0, 52: 0}  
dict_valores = {20: 2.5, 21: 3, 12: 6.5, 30: 6.5, 31: 7, 22: 12.5, 40: 20, 32: 41, 41: 63, 42: 980, 50: 11500, 51: 62000, 52: 40000000}  
# dict_premios = [2.5, 3, 6.5, 6.5, 7, 12.5, 20, 41, 63, 980, 11500, 62000, 40000000]
# chave do utilizador (fixa) comentar para pedir ao utilizador
listaNUser = [4, 16, 23, 35, 48]
listaEUser = [3, 11]
# chave do utilizador -> comentar para modo automático
# listaNUser = [0, 0, 0, 0, 0]      # chave do utilizador
# listaEUser = [0, 0]

listaNumeros = [0, 0, 0, 0, 0]    # 5 números do euromilhões durante 100 semanas
listaEstrelas = [0, 0]            # 2 número de estrelas

listaNUser = ler_int_lista(1, 50, 5)
listaEUser = ler_int_lista(1, 12, 2)
print(listaNUser, listaEUser)

# relatório
semanas_com_acerto = 0
total_gasto = 0.0
total_recebido = 0.0
total_numeros = 0
total_estrelas = 0
lista_acertos_numeros = [0, 0, 0, 0, 0]
lista_acertos_estrelas = [0, 0]

for semana in range(MAXSEMANAS+1):
    # sorteio
    total_gasto += 2.5
    listaNumeros = rnd_int_lista(1, 50, 5)
    listaEstrelas = rnd_int_lista(1, 12, 2)
    print(semana, listaNumeros, listaEstrelas)
    print(semana, listaNUser, listaEUser)
    clnum = compara_listas(listaNumeros, listaNUser)
    clest = compara_listas(listaEstrelas, listaEUser)
    print(clnum, " ", clest)
    if clnum > 0 or clest > 0:
        print("********** Semana com acerto: ", semana, "**********")
        semanas_com_acerto +=1
    total_numeros += clnum
    total_estrelas += clest
    if clnum > 0:
        lista_acertos_numeros[clnum-1] += 1
    if clest > 0:
        lista_acertos_numeros[clest-1] += 1
    premio = clnum * 10 + clest
    if premio > 11:
        dict_premios[premio] += 1
        total_recebido += dict_valores[premio]
        
# relatório 
print("\n**** Totais ****  para", MAXSEMANAS, "semanas  **** Totais ****\n")
print("Semanas com acerto: ", semanas_com_acerto, " -> ", semanas_com_acerto/MAXSEMANAS, "%")
print("Números certos: ", total_numeros, " -> ", total_numeros / (MAXSEMANAS * 5), "%")
print("Estrelas certas: ", total_estrelas, " -> ", total_estrelas / (MAXSEMANAS * 2), "%")
print(dict_premios)
k = 0
for x in dict_premios:
    if dict_premios[x] > 0:
        print("-> ", dict_premios[x], lista_premios[k], "prémio")
    k += 1
print("total gasto em apostas: ", total_gasto, "euros")
print("Total recebido em prémios: ", total_recebido, "euros  => ", round(total_recebido / total_gasto, 2), "%")

# fim do programa principal
