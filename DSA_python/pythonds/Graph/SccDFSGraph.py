from DSA_python.pythonds.Graph.DFSGraph import DFSGraph
from DSA_python.pythonds.Graph.Vertex import Vertex
from DSA_python.pythonds.basic.Stack import Stack


class SccDFSGraph(object):
    def __init__(self, lst, tup_lst):
        self.pos_edge = tup_lst
        self.normGraph = DFSGraph()
        self.buildNormal(self.normGraph, lst, tup_lst)
        self.trsGraph = DFSGraph()
        self.stack = Stack()

    @classmethod
    def buildNormal(cls, graph, lst, tup_lst):
        for _ in lst:
            graph.addVertex(_)

        for _ in tup_lst:
            graph.addEdge(*_)

    @classmethod
    def buildTranspose(cls, graph: DFSGraph, lst, tup_lst):
        for _ in lst:
            graph.addVertex(_)

        for _ in tup_lst:
            graph.addEdge(_[1], _[0])

    def SCCKosaraju(self):
        self._SCCKosaraju()
        self.print_forest(self.trsGraph)

    def _SCCKosaraju(self):
        self.normGraph.dfs()
        tmp = sorted(self.normGraph, key=lambda x: x.finTime, reverse=True)
        tmp = [_.id for _ in tmp]
        self.buildTranspose(self.trsGraph, tmp, self.pos_edge)
        self.trsGraph.dfs()

    def SCCTarjan(self):
        self.dfsTarjan_opt(self.normGraph)
        self.print_forest(self.normGraph)

    def dfsTarjan(self, graph):

        for vtx in graph:
            if not vtx.accessed:
                # self.stack.push(vtx)
                self._dfsTarjan(graph, vtx)

        tmp = sorted(graph, key=lambda x: (x.low, x.dfn))

        # for i in tmp:
        # print(f'{i.id}: dfn={i.dfn}, low={i.low}')

        root = None
        for _ in tmp:
            if _.low == _.dfn:
                graph.roots[_] = []
                root = _
            else:
                graph.roots[root].append(_)

    def _dfsTarjan(self, graph, stVtx: Vertex):
        graph.time += 1
        stVtx.dfn = graph.time
        stVtx.low = stVtx.dfn
        stVtx.accessed = True

        for nextVtx in stVtx.getConnections():
            if not nextVtx.accessed:
                nextVtx.pred = stVtx
                # self.stack.push(nextVtx)
                self._dfsTarjan(graph, nextVtx)

            stVtx.low = min(stVtx.low, nextVtx.low)

        for i in self.stack.content:
            print(f'{i.id}: dfn={i.dfn}, low={i.low}')
        print('------')

        # self.stack.pop()

    def SCCTarjan_opt(self):
        self.dfsTarjan_opt(self.normGraph)
        self.print_forest(self.normGraph)

    def dfsTarjan_opt(self, graph: DFSGraph):

        for vtx in graph:
            if not vtx.accessed:
                self.stack.push(vtx)
                self._dfsTarjan_opt(graph, vtx)

    def _dfsTarjan_opt(self, graph: DFSGraph, stVtx: Vertex):
        graph.time += 1
        stVtx.dfn = graph.time
        stVtx.low = stVtx.dfn
        stVtx.accessed = True

        for nextVtx in stVtx.getConnections():
            if not nextVtx.accessed:
                nextVtx.pred = stVtx
                self.stack.push(nextVtx)
                self._dfsTarjan_opt(graph, nextVtx)

            stVtx.low = min(stVtx.low, nextVtx.low)
        # print(f'{stVtx.id}: dfn={stVtx.dfn}, low={stVtx.low}')
        if stVtx.dfn == stVtx.low:
            tmpLst = []
            while True:
                tmpVtx = self.stack.pop()
                if tmpVtx != stVtx:
                    tmpLst.append(tmpVtx)
                else:
                    graph.roots[stVtx] = tmpLst
                    break
        else:
            pass

    @staticmethod
    def print_forest(graph):
        for root, verticesList in graph.roots.items():
            print(f'---SCC: {root.id}---')
            for vtx in verticesList:
                print(f'        {vtx.id}')


if __name__ == '__main__':
    #"""
    vtx_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    edge_list = [('A', 'B'),
                 ('A', 'C'),
                 ('A', 'G'),
                 ('B', 'H'),
                 ('H', 'A'),
                 ('C', 'F'),
                 ('G', 'F'),
                 ('F', 'A'),
                 ('C', 'D'),
                 ('D', 'E')
                 ]
    #"""
    """
    vtx_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
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
                 ('I', 'F'),
                 ('J', 'E')]
    """
    """
    vtx_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    edge_list = [('A', 'B'),
                 ('B', 'C'),
                 ('C', 'D'),
                 ('D', 'A'),
                 ('C', 'E'),
                 ('E', 'F'),
                 ('F', 'G'),
                 ('G', 'H'),
                 ('H', 'A')
                 ]
    """
    a_graph = SccDFSGraph(vtx_list, edge_list)
    a_graph.SCCTarjan_opt()
