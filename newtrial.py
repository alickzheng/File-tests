from collections import deque
from graphs import neighbours, print_grid_traversal
import graphs

g = graphs.ex_tree
def dfs_traversal(graph, s, goals = []):
    visited = []
    boundary = [s]
    while len(boundary) > 0:
        v = boundary.pop()
        for i in goals:
            if i == v:
                visited += [v]
                return visited
        visited += [v]
        for w in neighbours(v, graph): 
            if w not in visited and w not in boundary:
                boundary.append(w) 
    return visited
def reverse(lst):

    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse(lst[:-1])

def get_path(parent_list, s, e):
    reversed_path = [e]
    v = e
    print(parent_list)
    print(v)
    while v != s:
        reversed_path.append(parent_list[v])
        v = reversed_path[-1]
    path = reverse(reversed_path)
    return path

def bfs_traversal(graph, s, goals=[]):
    visited = []
    boundary = deque([s])
    p = [[] for _ in range(len(graph))]
    e = 0
    while len(boundary) > 0:
        v = boundary.popleft()
        if v in goals:
            visited += [v]
            e += v
            path = get_path(p, s, e)
            return path
        visited += [v]
        for w in neighbours(v, graph): 
            if w not in visited and w not in boundary:
                boundary.append(w)
                p[w] = v
#graphs.print_grid_traversal(g, 10, [0, 1, 2, 12, 13, 14, 15, 16, 17, 18, 28, 38, 39])
graphs.print_grid_traversal(g, 10, bfs_traversal(g, 0, {22}))
#9, 40, 49

#print(bfs_traversal(g, 0, {22}))