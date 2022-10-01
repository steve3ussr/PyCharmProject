from DSA_python.pythonds.Graph.DFSGraph import DFSGraph
from DSA_python.pythonds.Graph.Vertex import Vertex


def cutVtxTarjan(graph):
    for vtx in (_ for _ in graph if not _.accessed):
        graph.forest[vtx] = []
        vtx.pred = vtx
        _cutVtxTarjan(graph, vtx)

    for _ in graph:
        print(f'{_.id}: dfn={_.dfn}, low={_.low}')

    print('-----')
    for _ in graph.cut_vertices:
        print(f'CUT VERTEX: {_.id}: dfn={_.dfn}, low={_.low}')

    print('___FOREST___')
    for _ in graph.forest:
        print(_.id)

    return set([_.id for _ in graph.cut_vertices])


def _cutVtxTarjan(graph, curr_vtx: Vertex):
    curr_vtx.accessed = True
    graph.time += 1
    curr_vtx.dfn = graph.time
    curr_vtx.low = curr_vtx.dfn

    cnt = 0
    for next_vtx in curr_vtx:

        if not next_vtx.accessed:
            next_vtx.pred = curr_vtx
            cnt += 1
            _cutVtxTarjan(graph, next_vtx)

        if next_vtx != curr_vtx.pred:
            print(f'{curr_vtx.id} -> {next_vtx.id}')
            print(f'{curr_vtx.id}: min({curr_vtx.low}, {next_vtx.dfn})')
            curr_vtx.low = min(curr_vtx.low, next_vtx.low)

        if curr_vtx.dfn <= next_vtx.low and curr_vtx not in graph.forest:
            graph.cut_vertices.add(curr_vtx)

    if curr_vtx in graph.forest and cnt >= 2:
        graph.cut_vertices.add(curr_vtx)

def cutVtxTarjan_opt(graph):
    for vtx in (_ for _ in graph if not _.accessed):
        graph.forest[vtx] = []
        vtx.pred = vtx
        _cutVtxTarjan_opt(graph, vtx)

    for _ in graph:
        print(f'{_.id}: dfn={_.dfn}, low={_.low}')

    print('-----')
    for _ in graph.cut_vertices:
        print(f'CUT VERTEX: {_.id}: dfn={_.dfn}, low={_.low}')

    print('___FOREST___')
    for _ in graph.forest:
        print(_.id)

    return set([_.id for _ in graph.cut_vertices])


def _cutVtxTarjan_opt(graph, curr_vtx: Vertex):
    curr_vtx.accessed = True
    graph.time += 1
    curr_vtx.dfn = graph.time
    curr_vtx.low = curr_vtx.dfn

    cnt = 0
    for next_vtx in curr_vtx:

        if not next_vtx.accessed:
            next_vtx.pred = curr_vtx
            cnt += 1
            _cutVtxTarjan(graph, next_vtx)
            curr_vtx.low = min(curr_vtx.low, next_vtx.low)

        elif next_vtx != curr_vtx.pred:
            curr_vtx.low = min(curr_vtx.low, next_vtx.dfn)

        else:
            pass

        if curr_vtx.dfn <= next_vtx.low and curr_vtx not in graph.forest:
            graph.cut_vertices.add(curr_vtx)

    if curr_vtx in graph.forest and cnt >= 2:
        graph.cut_vertices.add(curr_vtx)


if __name__ == '__main__':
    vtx_list_1 = ['B', 'A', 'C', 'D', 'E', 'F', 'G', 'H']
    edge_list_1 = [['A', 'B'],
                   ['A', 'C'],
                   ['A', 'G'],
                   ['B', 'H'],
                   ['H', 'A'],
                   ['C', 'F'],
                   ['G', 'F'],
                   ['F', 'A'],
                   ['C', 'D'],
                   ['D', 'E']
                   ]
    vtx_list_2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    edge_list_2 = [['A', 'B'],
                   ['B', 'C'],
                   ['C', 'D'],
                   ['D', 'A'],
                   ['D', 'E'],
                   ['E', 'F'],
                   ['F', 'G'],
                   ['G', 'H'],
                   ['H', 'F']
                   ]
    vtx_list_3 = ['B', 'A', 'C', 'D', 'E']
    edge_list_3 = [['A', 'B'],
                   ['A', 'C'],
                   ['B', 'C'],
                   ['B', 'D'],
                   ['B', 'E'],
                   ['D', 'E'],
                   # ['E', 'F']
                   ]

    zsagraph = DFSGraph().build_undirected(vtx_list_1, edge_list_1)
    cutVtxTarjan(zsagraph)
