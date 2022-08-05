class Vertex(object):
    def __init__(self, key):
        self.id = key  # usually a string
        self.connectedTo = {}  # other vertices & edge weight
        self.__distance = 0
        self.__predecessor = None
        self.__accessed = False

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

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, i):
        self.__distance = i

    @property
    def pred(self):
        return self.__predecessor

    @pred.setter
    def pred(self, i):
        self.__predecessor = i

    @property
    def accessed(self):
        return self.__accessed

    @accessed.setter
    def accessed(self, i):
        self.__accessed = i


