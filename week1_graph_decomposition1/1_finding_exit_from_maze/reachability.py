import sys


class EzGraph():
    """
    Implementation of graph class with basic methods.
    Vertices of graph are represented as integers from 0 to n.
    Hello and authenticate on VSC
    """
    def __init__(self, adj_input, egde_list):
        self.adj_input = adj_input
        self.adjacency_list = self.create_adjacency_list()
        self.visited = [False] * len(self.adjacency_list)
        self.vertice_list = [i for i in range(len(self.adjacency_list))]
        self.egde_list = egde_list

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
        for edge in self.egde_list:
            if edge[0] == v:
                if not self.visited[edge[1]]:
                    self.explore(edge[1])
            elif edge[1] == v:
                if not self.visited[edge[0]]:
                    self.explore(edge[0])

    def DFS(self):
        """
        Implementation of Deep First Search Method from lecture
        """
        for i in self.vertice_list:
            self.visited[i] = False
        for i in self.vertice_list:
            if not self.visited[i]:
                self.explore(i)

    def reach(self, x: int, y: int) -> bool:
        """
        Method which checks if given vertices are reachable from each other

        Parameters:
        -----------
        x: int
            int representing the given vertice
        y: int
            int representing the given vertice

        Returns:
        --------
        1 if vertices are reachable, 0 if not
        """
        if self.visited[x] == 1 and self.visited[y] == 1:
            return 1
        else:
            return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    for i in range(len(data)):
        data[i] = data[i] - 1
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a].append(b)
        adj[b].append(a)
    graph = EzGraph(adj, edges)
    graph.explore(x)
    print(graph.reach(x, y))
