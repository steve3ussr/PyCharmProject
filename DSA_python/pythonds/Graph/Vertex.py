class Vertex(object):
    def __init__(self, key):
        self.id = key  # usually a string
        self.connectedTo = {}  # other vertices & edge weight

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + 'CONNECTED TO: \r' + str([_.id for _ in self.connectedTo])

    __repr__ = __str__

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo.get(nbr)
