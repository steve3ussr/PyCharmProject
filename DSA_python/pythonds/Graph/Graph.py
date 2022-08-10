from .Vertex import Vertex


class Graph(object):
    def __init__(self):
        self.vertDict = {}
        self.numVertices = 0
        self.numEdges = 0

    def addVertex(self, key, dist=0):
        if key in self:
            return

        self.numVertices += 1
        tmp = Vertex(key=key, dist=dist)
        self.vertDict[key] = tmp
        return tmp

    def __getitem__(self, item):
        return self.getVertex(item)

    def getVertex(self, item) -> Vertex:
        return self.vertDict.get(item)

    def __contains__(self, item):
        return item in self.vertDict

    def addEdge(self, fromVtx, toVtx, weight=0):
        self.numEdges += 1
        if fromVtx not in self.vertDict:
            self.addVertex(fromVtx)
        if toVtx not in self.vertDict:
            self.addVertex(toVtx)
        self.vertDict[fromVtx].addNeighbor(self.vertDict[toVtx], weight)

    def getVertices(self):
        return self.vertDict.keys()

    def __iter__(self):
        return iter(self.vertDict.values())

    def build_undirected(self, vtx_list, edge_list, dist=None):
        if dist is None:
            dist = sum([_[2] for _ in edge_list]) + 100

        for _ in vtx_list:
            self.addVertex(_, dist=dist)

        for _ in edge_list:
            self.addEdge(_[0], _[1], _[2])
            self.addEdge(_[1], _[0], _[2])

        return self

    def build_directed(self, vtx_list, edge_list, dist=None):
        if dist is None:
            dist = sum([_[2] for _ in edge_list]) + 100

        for _ in vtx_list:
            self.addVertex(_, dist=dist)

        for _ in edge_list:
            self.addEdge(_[0], _[1], _[2])

        return self




