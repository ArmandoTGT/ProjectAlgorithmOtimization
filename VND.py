from NeighborsResearch import NeighborsResearch

class VND:

    def run_vnd(self, paths, total_distances, matrix):
        neighborsResearch = NeighborsResearch(paths.copy(), total_distances.copy(), matrix)
        estruturas = ["2-opt", "swap", "insertion"]
        N = 0
        while(N <= 2):
            paths_new, total_distances_new = neighborsResearch.localResearch(estruturas[N], 1)
            if sum(total_distances_new.values()) < sum(total_distances.values()):
                print("entrou if",
                      total_distances_new,
                      paths_new,
                      sep = "\n\n")
                total_distances = total_distances_new
                paths = paths_new
                neighborsResearch = NeighborsResearch(paths.copy(), total_distances.copy(), matrix)
                N = 0
                
            else:
                N += 1

        return paths, total_distances