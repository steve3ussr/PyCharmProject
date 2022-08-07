from DSA_python.pythonds.Graph.DFSGraph import DFSGraph


class SccDFSGraph(object):
    def __init__(self, lst, tup_lst):
        self.pos_edge = tup_lst
        self.normGraph = DFSGraph()
        self.buildNormal(self.normGraph, lst, tup_lst)
        self.trsGraph = DFSGraph()

    @classmethod
    def buildNormal(cls, graph, lst, tup_lst):
        for _ in lst:
            graph.addVertex(_)

        for _ in tup_lst:
            graph.addEdge(*_)

    @classmethod
    def buildTranspose(cls, graph, lst, tup_lst):
        for _ in lst:
            graph.addVertex(_)

        for _ in tup_lst:
            graph.addEdge(_[1], _[0])

    def normalSCC(self):
        self.normGraph.dfs()
        tmp = sorted(self.normGraph, key=lambda x: x.finTime, reverse=True)
        tmp = [_.id for _ in tmp]
        print(tmp)
        print('----')
        self.buildTranspose(self.trsGraph, tmp, self.pos_edge)
        for k in self.trsGraph.vertDict:
            print(k)

        print('----')
        self.trsGraph.dfs()


if __name__ == '__main__':
    vtx_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    edge_list = [('A', 'B'),
                 ('B', 'E'),
                 ('E', 'A'),
                 ('D', 'B'),
                 ('E', 'D'),
                 ('D', 'G'),
                 ('G', 'E'),
                 ('B', 'C'),
                 ('C', 'C'),
                 ('C', 'F'),
                 ('F', 'H'),
                 ('H', 'I'),
                 ('I', 'F')]
    a_graph = SccDFSGraph(vtx_list, edge_list)
    a_graph.normalSCC()
