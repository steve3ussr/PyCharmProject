from DSA_python.pythonds.trees.MinBinaryHeapKV import MinBinaryHeapKV
from DSA_python.pythonds.Graph.Graph import Graph
from pprint import pprint


def Prim(graph, st_vtx_id):
    graph[st_vtx_id].distance = 0
    graph[st_vtx_id].pred = graph[st_vtx_id]
    heap = MinBinaryHeapKV().buildHeap([[_.distance, _.id] for _ in graph])

    while not heap.isEmpty():
        [curr_dist, curr_id] = heap.delMin()
        for next_inst in (_ for _ in graph[curr_id] if _.id in heap):
            new_dist = graph[curr_id][next_inst] + curr_dist
            if new_dist < next_inst.distance:
                next_inst.distance = new_dist
                next_inst.pred = graph[curr_id]
                heap.replace_key_by_val(next_inst.id, new_dist)

    pprint([f'{_.id} -> {_.distance} -> {st_vtx_id}, pred is {_.pred.id}' for _ in graph])


if __name__ == '__main__':
    vtx_list_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weight_list_1 = [
        ['A', 'B', 2],
        ['A', 'C', 3],
        ['B', 'C', 1],
        ['B', 'D', 1],
        ['B', 'E', 4],
        ['D', 'E', 1],
        ['E', 'F', 1],
        ['F', 'G', 1],
        ['C', 'F', 5]
    ]

    undirected_graph = Graph().build_undirected(vtx_list_1, weight_list_1)
    Prim(undirected_graph, 'A')
