#Uses python3

import sys

class EzGraph():

    def __init__(self, adj_input, egde_list):
        self.adj_input = adj_input
        self.adjacency_list = self.create_adjacency_list()
        self.visited = [False] * len(self.adjacency_list)
        self.vertice_list = [i for i in range(len(self.adjacency_list))]
        self.egde_list = egde_list
        # self.egdes_list = self.create_egde_list()
    def create_adjacency_list(self):
        adj_list = {}
        for i, v in enumerate(self.adj_input):
            adj_list[i] = v
        return adj_list

    # def create_egde_list(self):
    #     edge_list = {}
    #     for i, v in enumerate(self.egdes):
    #         edge_list[i] = v
    #     return edge_li

    def explore(self, v):
        self.visited[v] = True
        for edge in self.egde_list:
            if edge[0] == v:
                if not self.visited[edge[1]]:
                    self.explore(edge[1])
            elif edge[1] == v:
                if not self.visited[edge[0]]:
                    self.explore(edge[0])

    def DFS(self):
        for i in self.vertice_list:
            self.visited[i] = False
        for i in self.vertice_list:
            if not self.visited[i]:
                # problem: DFS will visit every vertice - so all will be visited
                # but we 
                self.explore(i)

    def reach(self, x, y):
        if self.visited[x] == 1 and self.visited[y] == 1:
            return 1
        else:
            return 0



# input_list = [[1, 3], [0, 2], [1, 3], [2, 0]]
# edges = [(0, 1), (2, 1), (3, 2), (0, 3)]
# graph = EzGraph(input_list, edges)
# print(graph.create_adjacency_list()) 
# print(graph.visited)
# print(graph.vertice_list)
# print(graph.DFS())
# print(graph.visited)
# print(graph.egdes)
# print(graph.create_egde_list())
# def reach(adj, x, y):
#     #write your code here



#     return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    for i in range(len(data)):
        data[i] = data[i] -1
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    # x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a ].append(b )
        adj[b ].append(a )
    graph = EzGraph(adj, edges)
    # print(graph.adjacency_list)
    # print(graph.egde_list)
    # print(graph.visited)
    # print(graph.vertice_list)
    # print(x)
    # print(y)
    graph.explore(x)
    # print(graph.visited)
    print(graph.reach(x, y))
#     print(adj)
#     print(edges)
#     print(x)
#     print(y)
