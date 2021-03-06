from NeighborsResearch import NeighborsResearch

class VND:

    def run_vnd(self, paths, total_distances, matrix):
        neighborsResearch = NeighborsResearch(paths.copy(), total_distances.copy(), matrix)
        estruturas = ["swap", "insertion", "2-opt"]
        N = 0
        while(N <= 2):
            paths_new, total_distances_new = neighborsResearch.localResearch(estruturas[N])
            if sum(total_distances_new.values()) < sum(total_distances.values()):
                total_distances = total_distances_new
                paths = paths_new
                # print("******if", paths, total_distances, estruturas[N], sep = "\n\n\n", end = "\n\n\n")
                neighborsResearch = NeighborsResearch(paths.copy(), total_distances.copy(), matrix)
                N = 0
                
            else:
                # print("######else", paths, total_distances, estruturas[N], sep = "\n\n\n", end = "\n\n\n")
                N += 1
                
        return paths, total_distances