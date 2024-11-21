def inserir_ordenado(): #criamos a função
    lista = [] #lista vazia
    a = "S" or "s" 
    i = 0
    while a == "S" or a == 's': #adiciona elementos a lista
        resposta = int(input("Insira elementos na lista: "))
        lista.insert(i, resposta)
        i = i + 1
        a = input("Deseja continuar? [S/N]")
    lista.sort() #ordena em forma crescente
    print(lista) #imprime a lista crescente
inserir_ordenado()