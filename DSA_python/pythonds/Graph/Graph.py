from .Vertex import Vertex


class Graph(object):
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        self.vertList[key] = Vertex(key)
        return self.vertList[key]

    def getVertex(self, item):
        return self.vertList.get(item)

    def __contains__(self, item):
        return item in self.vertList

    def addEdge(self, fromVtx, toVtx, weight=0):
        if fromVtx not in self.vertList:
            self.addVertex(fromVtx)
        if toVtx not in self.vertList:
            self.addVertex(toVtx)
        self.vertList[fromVtx].addNeighbor(self.vertList[toVtx], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())




