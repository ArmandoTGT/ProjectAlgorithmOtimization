from NeighborsResearch import NeighborsResearch

class VND:

    def run_vnd(self, paths, total_distances, matrix):
        neighborsResearch = NeighborsResearch(paths, total_distances, matrix)
        estruturas = ["2-opt", "swap", "insertion"]
        N = 0
        while(N >= 2):
            paths_new, total_distances_new = neighborsResearch.localResearch(estruturas[N], 10)
            if sum(total_distances.values()) < sum(total_distances_new.values()):
                total_distances = total_distances_new
                paths = paths_new
                N = 0
            else:
                N =+ 1

        return paths, total_distances