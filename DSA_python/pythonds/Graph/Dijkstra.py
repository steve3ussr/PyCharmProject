from pprint import pprint
from DSA_python.pythonds.Graph.Graph import Graph
from DSA_python.pythonds.trees.MinBinaryHeapKV import MinBinaryHeapKV


def Dijkstra(graph, st_vtx_id):

    graph[st_vtx_id].pred = graph[st_vtx_id]
    graph[st_vtx_id].distance = 0
    heap = MinBinaryHeapKV().buildHeap([[_.distance, _.id] for _ in graph])

    while not heap.isEmpty():

        curr_vtx_id = heap.delMin()[1]
        curr_vtx = graph[curr_vtx_id]

        for next_inst in (_ for _ in curr_vtx if _.id in heap):

            mid = curr_vtx.distance + curr_vtx[next_inst]
            if mid < next_inst.distance:
                next_inst.pred = curr_vtx
                next_inst.distance = mid
                heap.replace_key_by_val(next_inst.id, mid)

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

    undirected_graph = Graph().build_undirected(vtx_list_1, weight_list_1)
    Dijkstra(undirected_graph, 'A')
