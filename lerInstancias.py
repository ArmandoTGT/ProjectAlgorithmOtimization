class ler_instancias():
    
    def __init__(self, arquivo):
        instancias = open("instancias_teste/" + arquivo + '.txt', "r")
        lines = instancias.readlines()
        
        self.pontos = {}
        self.matrix = []
        
        self.dimensao = 0
        self.capacidade = 0
        
        linhaDePontos = False
        linhaDeMatrix = False
        
        for line in lines:
            line = line.replace('\n', '')
            
            if line.__contains__("DIMENSION:"):
                lineDividida = line.split()
                self.dimensao = lineDividida[1]
                
            if line.__contains__("CAPACITY:"):
                lineDividida = line.split()
                self.capacidade = lineDividida[1]        
              
            if line.__contains__("DEMAND_SECTION:") or linhaDePontos:
                linhaDePontos = True
                if line.__contains__("DEMAND_SECTION:"):
                    continue
                lineDividida = line.split()        
                if(len(lineDividida) == 0):
                    linhaDePontos = False
                else:
                    self.pontos[lineDividida[0]] = lineDividida[1]
                    
            if line.__contains__("EDGE_WEIGHT_SECTION") or linhaDeMatrix:
                linhaDeMatrix = True
                if line.__contains__("EDGE_WEIGHT_SECTION"):
                    continue
                lineDividida = line.split()        
                if(len(lineDividida) == 0):
                    linhaDeMatrix = False
                else:
                    self.matrix.append(lineDividida)    
            else:
                continue
    

    def get_pontos(self):       
        return self.pontos
    
    def get_matrix(self):       
        return self.matrix
    
    def get_dimensao(self):       
        return self.dimensao
    
    def get_capacidade(self):       
        return self.capacidade
    
        