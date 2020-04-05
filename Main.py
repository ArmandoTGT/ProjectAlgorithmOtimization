from ClosestNeighbor import ClosestNeighbor
from NeighborsResearch import NeighborsResearch
from VND import VND

import pandas as pd

f = open("instancias_teste/otimos", "r")
otimos = {}
for x in f:
  line = x.split(" ")
  otimos[line[0]] = int(line[2])


vnd = VND()
tabela = pd.DataFrame(index = otimos.keys(), columns = ["otimo", "HC - Média solução", 
"HC - Melhor Solução", "HC - Média Tempo", "HC - gap", "(HC + VND) - Média solução", 
"(HC + VND) - Melhor Solução", "(HC + VND) - Média Tempo", "(HC + VND) - gap"])

for situation in otimos:
    tabela["otimo"][situation] = otimos[situation]

    HeuristicAlgorithm = ClosestNeighbor(situation)
    HeuristicAlgorithm.closestNeighbor()

    paths = HeuristicAlgorithm.get_truck_path()
    total_distances = HeuristicAlgorithm.get_truck_total_distance()
    matrix = HeuristicAlgorithm.get_distance_matrix()
    
    tabela["HC - Melhor Solução"][situation] = sum(total_distances.values())
    tabela["HC - gap"][situation] = ((sum(total_distances.values()) - otimos[situation]) / otimos[situation]) * 100

    
    new_paths, new_total_distances = vnd.run_vnd(paths, total_distances, matrix)

    tabela["(HC + VND) - Melhor Solução"][situation] = sum(new_total_distances.values())
    tabela["(HC + VND) - gap"][situation] = ((sum(new_total_distances.values()) - otimos[situation]) / otimos[situation]) * 100

