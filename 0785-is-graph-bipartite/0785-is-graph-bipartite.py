class Solution:
    def __init__(self):
        self.grapho = []
    class node:
        def __init__(self, id):
            self.id = id
            self.color = 0
            self.d = 0

    def isBipartite(self, graph: List[List[int]]) -> bool:
        for i in range(len(graph)):
            self.grapho.append(self.node(i))
        
        for u in self.grapho:
            if u.color == 0:
                self.BFSVisit(u, graph)
        
        for u in self.grapho:
            for v in graph[u.id]:
                if u.d % 2 == self.grapho[v].d % 2:
                    return False
        
        return True
    
    
    def BFSVisit(self, s, graph):
        s.color = 1
        s.d = 0
        Q = []
        Q.append(s)
        while len(Q) != 0:
            u = Q.pop(0)
            for v in graph[u.id]:
                if self.grapho[v].color == 0:
                    self.grapho[v].color = 1
                    self.grapho[v].d = u.d + 1

                    Q.append(self.grapho[v])
            

        