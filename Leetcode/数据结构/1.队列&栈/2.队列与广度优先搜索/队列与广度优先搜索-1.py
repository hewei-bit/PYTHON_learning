from queue import Queue


def BFS(adj, start):
    visited = set()
    q = Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        print(u)
        for v in adj.get(u, []):
            if v not in visited:
                visited.add(v)
                q.put(v)


graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
BFS(graph, 1)
