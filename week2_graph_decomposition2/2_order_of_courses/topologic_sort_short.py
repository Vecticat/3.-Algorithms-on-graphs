import sys
from typing import Counter

DIRECTED = True
class EzGraph():
    """
    Implementation of graph class with basic methods.
    Vertices of graph are represented as integers from 0 to n.
    Hello and authenticate on VSC
    """
    def __init__(self, adj_input, egde_list):
        self.n_v = len(adj_input)
        self.adj_input = adj_input
        self.adjacency_list = self.create_adjacency_list()
        self.visited = [False] * self.n_v
        self.vertice_list = [i for i in range(self.n_v)]
        self.egde_list = egde_list
        self.postvisit_list = [0 for i in range(self.n_v)]
        self.clock = 1


    def create_adjacency_list(self):
        """
        Creates adjacency list - converts from representation of graph
        from: list of list
        to: dict of list
        Returns:

        --------
        adj_list: dict
            dict with representation of graph as adjacency list
        """

        adj_list = {}
        for i, v in enumerate(self.adj_input):
            adj_list[i] = v
        return adj_list


    def explore(self, v: int):
        """
        Implementation of explore method from lecture:
        For given vertices explore all vertices reachable from it

        Parameters:
        -----------
        v: int
            int representing the given vertices in graph

        """
        self.visited[v] = True

        # rewrite this fragment?
        # zamiast leciec po edgu: lecmy po adj _list? moze szybsze -> nie musimy robic tam ifa -> bo wiadomo ze jest co jest

        # for edge in self.egde_list: # czy my musimy leiec po kazdym edgu i tam szukac dobrego?
        #     if edge[0] == v:   # O(1)
        #         if not self.visited[edge[1]]:
        #             self.explore(edge[1])

        # gdyby nie to next pomysl: nie zamieniajmy adj matrix na adj list, tylko od razu na tym

        for value in self.adjacency_list[v]:
            if not self.visited[value]:
                self.explore(value)


        self.postvisit_list[v] = self.clock #O(1)

        self.visit_list.append(v+1)#O(1)
        self.clock += 1 #O(1)

    def DFS(self):
        """
        Implementation of Deep First Search Method from lecture
        """

        self.visit_list = [] # better idea - necessary only in this function so
        for i in self.vertice_list:
            if not self.visited[i]:
                self.explore(i)

    def TopologicalOrder(self):
        """
        Implementatio onf Topological Order
        """
        self.DFS()
        print(*self.visit_list[::-1])




if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    for i in range(len(data)):
        data[i] = data[i] - 1
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a].append(b)


    graph = EzGraph(adj, edges)
    graph.TopologicalOrder()
    # print(graph.adjacency_list)
    # print(adj)