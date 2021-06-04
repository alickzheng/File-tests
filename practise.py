#backtracking algorithms
def atk(r1, c1, r2, c2):
    return r1 == r2 or c1 == c2 or abs(c1 - c2) == abs(r1 - r2)

def valid(config):
    n = len(config)
    for i in range(n):
        for j in range(i + 1, n):
            if atk(config(i), i, config(j), j):
                return False
    return True

def is_atk(row, col, p):
    n = 0
    while n != len(p):
        if atk(row, col, p[n], n):
            return True
        else:
            n += 1
    return False
        
def options(p, n):
    res = []
    col = len(p)
    for row in range(n):
        if not is_atk(row, col, p):
            res += [row]
    return res

def nqueen(n, p = []):
    if len(p) == n:
        return [p]
    else:
        res = []
        for o in options(p, n):
            res += nqueen(n, p + [o])
        return res

#recursions
def rgcd(x1, x2):
    if x2 == 0:
        return x1
    else:
        return rgcd(x2, x1%x2)

#sorting algorithms
test = [0, 9 ,8 ,7 ,6 ,3, 2, 1]
def rSelSort(lst):
    '''
    >>> rSelSort(test)
    [0, 1, 2, 3, 6, 7, 8, 9]
    '''
    res = []
    if len(lst) <= 1:
        return lst
    else:
        index = lst.index(min(lst))
        lst[0], lst[index] = lst[index], lst[0]
        res.append(lst[0])
        return res + rSelSort(lst[1:])

def insertSort(lst):
    n = len(lst)
    if len(lst) <= 1:
        return lst
    else:
        for i in range(n):
            if i > 1:
                for j in range(len(lst[:i])):
                    if lst[i] < lst[j]:
                        lst[i], lst[j] = lst[j], lst[i]
        return lst

#spanning tress
def empty_graph(n):
    res = [[0 for _ in range(n)] for _ in range(n)]
    return res

graph = [[0, 1, 1, 0, 0], 
        [1, 0, 0, 0, 0], 
        [1, 0, 0, 1, 0], 
        [0, 0, 1, 1, 0], 
        [0, 0, 1, 0, 0]]

def friend(graph, v1, v2):
    if graph[v1][v2] == 1:
        return True
    else:
        return False

def secFriend(graph, v1, v2):
    for i in range(len(graph[v1])):
        if graph[v1][i] == 1:
            if graph[i][v2] == 1:
                return True
    return False

def hasPath(graph, v1, v2):
    pass

def red_echelon(matrix):
    pass

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True) 