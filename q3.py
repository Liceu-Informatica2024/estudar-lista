def contar_ocorrências(): #criamos a funcao
    lista = [] #lista vazia
    a = "S" or "s" 
    i = 0
    while a == "S" or a == 's': #adiciona elementos a lista
        resposta = int(input("Insira elementos na lista: "))
        lista.insert(i, resposta)
        i = i + 1
        a = input("Deseja continuar? [S/N]")   
    n = int(input('Escreva o num que vc quer contar: ')) #pergunta ao usuario qual numero quer contar
    print(lista.count(n)) #conta e imprime as ocorrencias
contar_ocorrências()
