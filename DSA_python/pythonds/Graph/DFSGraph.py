from .Graph import Graph
from .Vertex import Vertex


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0
        self.forest = {}
        self._tmp_root = None
        self.cut_vertices = set()

    def dfs(self):
        for vtx in self:
            if not vtx.accessed:
                self._tmp_root = vtx
                self.forest[vtx] = []
                self.dfsVisit(vtx)

    def dfsVisit(self, stVtx: Vertex):
        self.time += 1
        stVtx.accessed = True
        stVtx.disTime = self.time

        for nextVtx in stVtx.getConnections():
            if nextVtx.accessed:
                continue
            else:

                self.forest[self._tmp_root].append(nextVtx)
                nextVtx.pred = stVtx
                self.dfsVisit(nextVtx)
        self.time += 1
        stVtx.finTime = self.time
