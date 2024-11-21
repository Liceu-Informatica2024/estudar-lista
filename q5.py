def ordenar_lista(): 
    listaA = [] #lista vazia
    a = "S" or "s" 
    i = 0
    while a == "S" or a == 's': #adiciona elementos a lista
        resposta = int(input("Insira elementos na lista: "))  
        listaA.insert(i, resposta)
        i = i + 1
        a = input("Deseja continuar? [S/N]")   
    
    
    listaB = listaA[:] #separa a lista em duas
    listaA.sort() #deixa em ordem crescente
    print(listaA) #imprime
    listaB.reverse() #deixa em ordem descrescente  
    print(listaB) #imprime
ordenar_lista()