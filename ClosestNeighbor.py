from lerInstancias import ler_instancias
        
class ClosestNeighbor:
    def __init__(self):
        loader = ler_instancias("P-n16-k8")
        self._demand = loader.get_pontos()
        self._distance_matrix = loader.get_matrix()
        self._matrix_dimension = loader.get_dimensao()
        self._truck_max_capacity = loader.get_capacidade()
        
        # Normalização dos valores para integer
        for i in range(len(self._distance_matrix)):
            for j in range(len(self._distance_matrix[i])):
                self._distance_matrix[i][j] = int(self._distance_matrix[i][j])
        for key in self._demand:
            self._demand[key] = int(self._demand[key])
        self._matrix_dimension = int(self._matrix_dimension)
        self._truck_max_capacity = int(self._truck_max_capacity)

        # Caminhos a se tomar
        self._truck_path = {}

    def closestNeighbor(self):
        # O caminhão sai do CD, q é o ponto zero
        truck_weight = int(self._truck_max_capacity)
        i = 0
        truck = 0
        visited_points = [0]
        self._truck_path[truck] = [0]
        total_distance = 0
        print(self._demand)
        while len(visited_points) < len(self._demand):
            closest_distance = 99999999
            # O primeiro ponto mais próximo é ele mesmo
            closest_node = i
            # Flag que diz se o caminhão tem capacidade de visitar outro ponto, antes de voltar ao CD
            truck_capacity = False
            for j in range(len(self._distance_matrix[i])):
                # Desconsiderando ele mesmo, procuramos o ponto que tenha a menor distância, caiba no caminhão e
                # ainda não tenha sido visitado
                if j not in visited_points and closest_distance > self._distance_matrix[i][j] and truck_weight - self._demand[str(j)] >= 0:
                    truck_capacity = True
                    closest_node = j
                    closest_distance = self._distance_matrix[i][j]
            
            if truck_capacity:
                truck_weight = truck_weight - self._demand[str(closest_node)]
                self._truck_path[truck].append(closest_node)
                total_distance += closest_distance
                visited_points.append(closest_node)
                # Se o próximo passo acabar o while, já adicionamos o CD para ele voltar e seu peso final
                if not len(visited_points) < len(self._demand):
                    self._truck_path[truck].append(0)
                    total_distance += self._distance_matrix[closest_node][0]
                    self._truck_path[truck].append(truck_weight)
                    self._truck_path[truck].append(total_distance)
                i = closest_node

            else:
                # Caminhão não conseguiu e voltou para o CD, adicionamos no final, quanto ficou sobrando e ele vai percorrer
                self._truck_path[truck].append(0)
                total_distance += self._distance_matrix[closest_node][0]
                self._truck_path[truck].append(truck_weight)
                self._truck_path[truck].append(total_distance)
                truck_weight = self._truck_max_capacity
                # Novo caminhão que vai ter que sair do CD
                truck += 1
                total_distance = 0
                self._truck_path[truck] = []
                self._truck_path[truck].append(0)
            # print(sorted(visited_points))
        # print(self._truck_path)

    def printPaths(self):
        for truck in self._truck_path:
            print("Caminhão", truck)
            print("Caminho de pontos", self._truck_path[truck][:-2])
            print("Lotação do caminhão", self._truck_max_capacity - self._truck_path[truck][-2])
            print("Distância percorrida", self._truck_path[truck][-1], '\n')

                    


                
HeuristicAlgorithm = ClosestNeighbor()
HeuristicAlgorithm.closestNeighbor()
HeuristicAlgorithm.printPaths()
