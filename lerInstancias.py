def carrega_instancias(arquivo):
    instancias = open("instancias_teste/arquivo.txt", "r")
    lines = instancias.readlines()
    
    pontos = {}
    matrix = []
    
    dimensao = 0
    capacidade = 0
    
    linhaDePontos = False
    linhaDeMatrix = False
    
    for line in lines:
        line = line.replace('\n', '')
        
        if line.__contains__("DIMENSION:"):
            lineDividida = line.split()
            dimensao = lineDividida[1]
            
        if line.__contains__("CAPACITY:"):
            lineDividida = line.split()
            capacidade = lineDividida[1]        
          
        if line.__contains__("DEMAND_SECTION:") or linhaDePontos:
            linhaDePontos = True
            if line.__contains__("DEMAND_SECTION:"):
                continue
            lineDividida = line.split()        
            if(len(lineDividida) == 0):
                linhaDePontos = False
            else:
                pontos[lineDividida[0]] = lineDividida[1]
                
        if line.__contains__("EDGE_WEIGHT_SECTION") or linhaDeMatrix:
            linhaDeMatrix = True
            if line.__contains__("EDGE_WEIGHT_SECTION"):
                continue
            lineDividida = line.split()        
            if(len(lineDividida) == 0):
                linhaDeMatrix = False
            else:
                matrix.append(lineDividida)    
        else:
            continue
    
    return pontos, matrix, dimensao, capacidade
        