from pprint import pprint
from DSA_python.pythonds.Graph.Graph import Graph
from DSA_python.pythonds.Graph.Vertex import Vertex
from DSA_python.pythonds.trees.MinBinaryHeapKV import MinBinaryHeapKV


def Dijkstra(graph, st_vtx_id):
    heap = MinBinaryHeapKV()
    tmp = [[_.distance, _.id] for _ in graph]
    heap.buildHeap(tmp)

    curr_vtx = graph.getVertex(st_vtx_id)
    st_vtx = curr_vtx
    st_vtx.pred = st_vtx
    curr_vtx_id = st_vtx_id
    curr_vtx.distance = 0
    heap.del_val(curr_vtx_id)

    while not heap.isEmpty():

        for vtx_inst in curr_vtx.getConnections():
            if vtx_inst.id in heap:

                mid = curr_vtx.distance + curr_vtx.getWeight(vtx_inst)
                dir = vtx_inst.distance
                if mid < dir:
                    vtx_inst.pred = curr_vtx
                    vtx_inst.distance = mid

                heap.replace_key_by_val(vtx_inst.id, vtx_inst.distance)

        curr_vtx_id = heap.delMin()[1]
        curr_vtx = graph.getVertex(curr_vtx_id)

    pprint([f'{_.id} -> {_.distance} -> {st_vtx_id}, pred is {_.pred.id}' for _ in graph])


if __name__ == '__main__':
    vtx_list_1 = ['A', 'B', 'C', 'D', 'E', 'F']
    weight_list_1 = [
        ['A', 'F', 1],
        ['A', 'B', 1],
        ['A', 'E', 2],
        ['E', 'F', 2],
        ['E', 'D', 3],
        ['B', 'D', 1],
        ['B', 'C', 1],
        ['C', 'D', 5],
        ['D', 'F', 5],
        ['A', 'D', 3],
    ]

    def build_undirected_graph(vtx, edge):
        graph = Graph()
        max_dist = sum([_[2] for _ in edge]) + 100

        for _ in vtx:
            graph.addVertex(_, dist=max_dist)

        for _ in edge:
            graph.addEdge(_[0], _[1], _[2])
            graph.addEdge(_[1], _[0], _[2])

        return graph

    undirected_graph = build_undirected_graph(vtx_list_1, weight_list_1)
    Dijkstra(undirected_graph, 'A')
