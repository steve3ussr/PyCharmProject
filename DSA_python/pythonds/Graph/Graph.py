from .Vertex import Vertex


class Graph(object):
    def __init__(self):
        self.vertDict = {}
        self.numVertices = 0
        self.numEdges = 0

    def addVertex(self, key):
        if key in self:
            return

        self.numVertices += 1
        tmp = Vertex(key)
        self.vertDict[key] = tmp
        return tmp

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




