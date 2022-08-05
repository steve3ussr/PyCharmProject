from DSA_python.pythonds.Graph.Graph import Graph
from DSA_python.pythonds.basic.Queue import Queue
from DSA_python.graph_learn.buildGraph_wordLadder import buildGraphWordLadder


def BFS_wordLadder(stVtx):
    """

    :param stVtx: start vertex id
    :return: a path
    """
    layer_list = [stVtx]

    while layer_list:
        next_list = []
        for crrtVtx in layer_list:
            crrtVtx.accessed = True

            for nbr in crrtVtx.getConnections():
                if nbr.accessed:
                    continue
                else:
                    nbr.distance = crrtVtx.distance + 1
                    nbr.accessed = True
                    nbr.pred = crrtVtx
                    next_list.append(nbr)

        layer_list = next_list


def Book_wordLadder(stVtx):
    """

    :param stVtx: start vertex id
    :return: a path
    """
    vtxQ = Queue()
    vtxQ.enqueue(stVtx)

    while not vtxQ.isEmpty():
        crrtVtx = vtxQ.dequeue()
        crrtVtx.accessed = True
        for nbr in crrtVtx.getConnections():
            if nbr.accessed:
                continue
            else:
                nbr.distance = crrtVtx.distance + 1
                nbr.pred = crrtVtx
                nbr.accessed = True
                vtxQ.enqueue(nbr)


def backTraverse(aVtx):
    tmp = aVtx
    while tmp.pred:
        print(tmp.getId())
        tmp = tmp.pred
    print(tmp.getId())


if __name__ == '__main__':
    from time import time as tt


    def timer(func):
        def timer_inner():
            st = tt()
            func()
            end = tt()
            print(f'{(end-st) * 1000}ms')
        return timer_inner


    @timer
    def BFS_main():
        for i in range(31):
            aGraph = buildGraphWordLadder('fool', 'sage')
            BFS_wordLadder(aGraph.getVertex('fool'))
            backTraverse(aGraph.getVertex('sage'))
            del aGraph

    @timer
    def Book_main():
        for i in range(31):
            aGraph = buildGraphWordLadder('fool', 'sage')
            Book_wordLadder(aGraph.getVertex('fool'))
            backTraverse(aGraph.getVertex('sage'))
            del aGraph

    BFS_main()
    Book_main()
