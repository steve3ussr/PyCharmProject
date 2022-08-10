class Vertex(object):
    def __init__(self, key, dist=0):
        self.id = key  # usually a string
        self.connectedTo = {}  # other vertices & edge weight
        self.__distance = dist
        self.__predecessor = None
        self.__accessed = False
        self.__discoverTime = None
        self.__finishTime = None
        self.__low = None
        self.__dfn = None

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + 'CONNECTED TO: \r' + str([_.id for _ in self.connectedTo])

    __repr__ = __str__

    def __iter__(self):
        return iter(self.getConnections())

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo.get(nbr)

    def __getitem__(self, nbr):
        return self.getWeight(nbr)

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

    @property
    def disTime(self):
        return self.__discoverTime

    @disTime.setter
    def disTime(self, i):
        self.__discoverTime = i

    @property
    def finTime(self):
        return self.__finishTime

    @finTime.setter
    def finTime(self, i):
        self.__finishTime = i

    @property
    def low(self):
        return self.__low

    @low.setter
    def low(self, i):
        self.__low = i

    @property
    def dfn(self):
        return self.__dfn

    @dfn.setter
    def dfn(self, i):
        self.__dfn = i



