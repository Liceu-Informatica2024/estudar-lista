def encontrar_min_max():
    lista = [] #lista vazia
    a = "S" or "s" 
    i = 0
    while a == "S" or a == 's': #adiciona elementos a lista
        resposta = int(input("Insira elementos na lista: "))
        lista.insert(i, resposta)
        i = i + 1
        a = input("Deseja continuar? [S/N]")   
    tupla = (lista) #criamos uma tupla
    print("Menor valor: ",min(tupla)) #retorna o menor valor 
    print("Máximo valor: ",max(tupla)) #retorna o maior valor
encontrar_min_max()