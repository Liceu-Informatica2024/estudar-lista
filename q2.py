def reverter_lista():
    lista = [] #lista vazia
    a = "S" or "s" 
    i = 0
    while a == "S" or a == 's': #adiciona elementos a lista
        resposta = str(input("Insira elementos na lista: "))
        lista.insert(i, resposta)
        i = i + 1
        a = input("Deseja continuar? [S/N]")
    lista.reverse() #ordena em ordem decrescente
    print(lista) #imprime os valores
reverter_lista()