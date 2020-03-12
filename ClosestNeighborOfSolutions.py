from ClosestNeighbor import ClosestNeighbor

class ClosestNeighborOfSolutions:
    
    def __init__(self):
        
        HeuristicAlgorithm = ClosestNeighbor()
        HeuristicAlgorithm.closestNeighbor()
        self._paths = HeuristicAlgorithm.get_truck_path()
        self._total_distances = HeuristicAlgorithm.get_truck_total_distance()
        self._matrix = HeuristicAlgorithm.get_distance_matrix()

    def closestNeighbor(self, solution, number_of_neighbours):
        if solution == "2-opt":
            for iteration in range(number_of_neighbours):
                for i in range(self.HeuristicAlgorithm.get_number_trucks()):
                    self._paths[i] = self.opt_2(self._paths[i], self._matrix, self._total_distances[i])
                    
        elif solution == "swap":
            for iteration in range(number_of_neighbours):
                for i in range(self.HeuristicAlgorithm.get_number_trucks()):
                    self._paths[i] = self.swap(self._paths[i], self._matrix, self._total_distances[i])
    
        elif solution == "insertion":
            for iteration in range(number_of_neighbours):
                for i in range(self.HeuristicAlgorithm.get_number_trucks()):
                    self._paths[i] = self.insertion(self._paths[i], self._matrix, self._total_distances[i])
    
    
    def opt_2(self, route, matrix, current_total_distance):
        best = [current_total_distance, 0, 0]    
        for p1_a1 in range(0, len(route)-4):
            p2_a1 = p1_a1 +1
            #print(route[p1_a1], route[p2_a1])
            for p1_a2 in range(p2_a1+2, len(route)-1):
                p2_a2 = p1_a2 +1
                new_total_distance = current_total_distance                                    
                print(new_total_distance)
                new_total_distance -= matrix[route[p1_a1]][route[p2_a1]]
                print(new_total_distance)                    
                new_total_distance -= matrix[route[p1_a2]][route[p2_a2]]
                print(new_total_distance)
                             
                new_total_distance += matrix[route[p1_a1]][route[p1_a2]]
                print(matrix[route[p1_a1]][route[p1_a2]], "====")
                print(new_total_distance)
                new_total_distance += matrix[route[p2_a1]][route[p2_a2]]
                print(matrix[route[p2_a1]][route[p2_a2]], "======")
                print(new_total_distance)
                #print(route[p1_a1], route[p2_a1], route[p1_a2], route[p2_a2])
                if(new_total_distance < best[0]):
                    best[0] = new_total_distance
                    best[1] = p2_a1
                    best[2] = p1_a2
        
        if(best[0] < current_total_distance):
            print(best[0])
            route[best[1]], route[best[2]] = route[best[2]], route[best[1]]
            
        return route
    
    def insertion(self, route, matrix, current_total_distance):
        best = [current_total_distance, 0, 0]
        for index in range(0, len(route)):
             if route[index] != 0:
                 for index_insertion in range(1, len(route)-1):
                     new_total_distance = current_total_distance 
                     print(route[index], route[index_insertion])
                     if route[index-1] != route[index_insertion] and route[index] != route[index_insertion] and route[index+1] != route[index_insertion]:
                         
                         
                         new_total_distance -= matrix[route[index]][route[index+1]]
                         new_total_distance -= matrix[route[index]][route[index-1]]                         
                         new_total_distance -= matrix[route[index_insertion]][route[index_insertion+1]]
                         
                         new_total_distance += matrix[route[index-1]][route[index+1]]
                         new_total_distance += matrix[route[index_insertion+1]][route[index]]
                         new_total_distance += matrix[route[index]][route[index_insertion]]
                         
                         
                         if(new_total_distance < best[0]):
                             best[0] = new_total_distance
                             best[1] = index
                             best[2] = index_insertion
        
        
        if(best[0] < current_total_distance):
            print(best[0])
            aux = route.pop(best[1])            
            route.insert(best[2], aux)
            
        
        return route            
            
    def swap(self, route, matrix, current_total_distance):
        best = [current_total_distance, 0, 0]
        for index in range(1, len(route)-1):             
            for index_swap in range(index+1, len(route)-1):
                new_total_distance = current_total_distance                                        
                
                new_total_distance -= matrix[route[index]][route[index-1]]                    
                new_total_distance -= matrix[route[index_swap]][route[index_swap+1]]
                if(route[index+1] != route[index_swap]):
                    new_total_distance -= matrix[route[index]][route[index+1]]
                    new_total_distance -= matrix[route[index_swap]][route[index_swap-1]]
               
                    new_total_distance += matrix[route[index]][route[index_swap-1]]           
                    new_total_distance += matrix[route[index_swap]][route[index+1]]               
                new_total_distance += matrix[route[index]][route[index_swap+1]]
                new_total_distance += matrix[route[index-1]][route[index_swap]]
               
                if(new_total_distance < best[0]):
                    best[0] = new_total_distance
                    best[1] = index
                    best[2] = index_swap
        
        if(best[0] < current_total_distance):
            print(best[0])
            route[best[1]], route[best[2]] = route[best[2]], route[best[1]]
            
        return route
    
    def teste(self):
        "0+21+7+21+29 = 78"
        #[0, 1, 10, 12, 15, 4, 11, 3, 8, 18, 14, 0] 172
        
        #[0, 21, 16, 1, 10, 13, 0] 72
        #[0, 21, 16, 13, 10, 1, 0] 71 - opt2
        #[0, 21, 16, 13, 10, 1, 0] 71 - swap
        solucao = [0, 21, 16, 1, 10, 13, 0]
        distancia = 71
        print("Solução inicial", solucao)
        print("Distância total", distancia)
        new_route = self.opt_2(solucao, self._matrix, distancia)
        print("Solução vizinha", new_route)
    

buscaLocal = ClosestNeighborOfSolutions()

buscaLocal.teste()


        
    
   