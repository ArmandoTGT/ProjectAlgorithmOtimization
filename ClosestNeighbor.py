from lerInstancias import ler_instancias
import random
     
class ClosestNeighbor:
    def __init__(self, situation):
        loader = ler_instancias(situation)
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
        self._truck = 0
        self._truck_path = {}
        self._truck_capacity = {}
        self._truck_total_distance = {}

    def closestNeighbor(self):
        # O caminhão sai do CD, q é o ponto zero
        truck_weight = int(self._truck_max_capacity)
        i = 0
        visited_points = [0]
        self._truck_path[self._truck] = [0]
        total_distance = 0
        #print(self._demand)
        while len(visited_points) < len(self._demand):
            closest_distance = 99999999
            # O primeiro ponto mais próximo é ele mesmo
            closest_node = i
            # Flag que diz se o caminhão tem capacidade de visitar outro ponto, antes de voltar ao CD
            truck_capacity = False
            list_closest_nodes = []
            list_closest_distance = []
            for j in range(len(self._distance_matrix[i])):
                # Desconsiderando ele mesmo, procuramos todos os pontos que caibão no caminhão e ainda não tenha sido visitado
                if j not in visited_points and truck_weight - self._demand[str(j)] >= 0:
                    truck_capacity = True
                    list_closest_nodes.append(j)
                    list_closest_distance.append(self._distance_matrix[i][j])

            if truck_capacity:
                # Escolha aleatoria dos até 5 nós mais próximos
                list_closest_nodes, list_closest_distance = self.sort_parallel_list(list_closest_nodes, list_closest_distance)
                list_closest_nodes, list_closest_distance = list_closest_nodes[:5], list_closest_distance[:5]

                choosen_node = random.randint(0,len(list_closest_nodes) - 1)
                closest_node =  list_closest_nodes[choosen_node]
                closest_distance = list_closest_distance[choosen_node]

                # Encaixe do nó na rota
                truck_weight = truck_weight - self._demand[str(closest_node)]
                self._truck_path[self._truck].append(closest_node)
                total_distance += closest_distance
                visited_points.append(closest_node)
                # Se o próximo passo acabar o while, já adicionamos o CD para ele voltar e seu peso final
                if not len(visited_points) < len(self._demand):
                    self._truck_path[self._truck].append(0)
                    total_distance += self._distance_matrix[closest_node][0]
                self._truck_capacity[self._truck] = truck_weight
                self._truck_total_distance[self._truck] = total_distance
                # Local onde começaremos a verificação do próximo ponto é o nó mais próximo
                i = closest_node

            else:
                # Caminhão não conseguiu e voltou para o CD, adicionamos no final, quanto ficou sobrando e ele vai percorrer
                self._truck_path[self._truck].append(0)
                total_distance += self._distance_matrix[closest_node][0]
                self._truck_capacity[self._truck] = truck_weight
                self._truck_total_distance[self._truck] = total_distance
                truck_weight = self._truck_max_capacity
                # Novo caminhão que vai ter que sair do CD
                self._truck += 1
                total_distance = 0
                self._truck_path[self._truck] = []
                self._truck_path[self._truck].append(0)
                i = 0

    def sort_parallel_list(self, key, value):
        temp = sorted(zip(key,value), key=lambda i: i[1])

        key = []
        value = []

        for a_temp, b_temp in temp:
            key.append(a_temp)
            value.append(b_temp)
        return key, value

    def printPaths(self):
        for truck in self._truck_path:
            print("Caminhão", truck)
            print("Caminho de pontos", self._truck_path[truck])
            print("Espaço no caminhão", self._truck_capacity[truck])
            print("Distância percorrida", self._truck_total_distance[truck], '\n')

    def get_route(self, truck):
        return self._truck_path[truck]
    
    def get_route_total_distance(self, truck):
        return self._truck_total_distance[truck]

    def get_truck_path(self):
        return self._truck_path
    
    def get_truck_capacity(self):
        return self._truck_capacity
    
    def get_truck_total_distance(self):
        return self._truck_total_distance

    def get_number_of_trucks(self):
        return self._truck

    def get_distance_matrix(self):
        return self._distance_matrix              


HeuristicAlgorithm = ClosestNeighbor("P-n19-k2")
HeuristicAlgorithm.closestNeighbor()
paths = HeuristicAlgorithm.get_truck_path()
capacities = HeuristicAlgorithm.get_truck_capacity()
total_distances = HeuristicAlgorithm.get_truck_total_distance()
trucks = HeuristicAlgorithm.get_number_of_trucks()

#rint(paths, total_distances, sep = "\n\n\n\n\n")
'''
def __init__(self):
    self.HeuristicAlgorithm = ClosestNeighbor()
    HeuristicAlgorithm.closestNeighbor()
    self._paths = HeuristicAlgorithm.get_truck_path()
    self._total_distances = HeuristicAlgorithm.get_truck_total_distance()
    self._matrix = HeuristicAlgorithm.get_distance_matrix()

def closestNeighbor(self, solution, number_of_neighbours):
    if solution == "insertion":
        for iteration in range(number_of_neighbours):
            for i in range(self.HeuristicAlgorithm.get_number_trucks()):
                self._paths[i] = self.insertion(self._paths[i], self._matrix, self._total_distances[i])
    
    elif solution == "swap":
        for iteration in range(number_of_neighbours):
            for i in range(self.HeuristicAlgorithm.get_number_trucks()):
                self._paths[i] = self.insertion(self._paths[i], self._matrix, self._total_distances[i])

    elif solution == "2-opt":
        for iteration in range(number_of_neighbours):
            for i in range(self.HeuristicAlgorithm.get_number_trucks()):
                self._paths[i] = self.insertion(self._paths[i], self._matrix, self._total_distances[i])
'''
