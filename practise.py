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



#general backtracking algo
'''
def solutions(completed, options, part=[]):
    if completed(part):
        return [part]
    else:
        res = []
        for o in options(part):
            augmented = part+[o]
            res += solutions(completed, options, augmented)
        return res
'''
#if __name__=='__main__':
    #import doctest
    #doctest.testmod(verbose=True) 

def solutions(completed, options, part=[]):
    if completed(part):
        return [part]
    else:
        res = []
        for o in options(part):
            augmented = part+[o]
            res += solutions(completed, options, augmented)
        return res

def neighbour(vertex, graph):
    res = [i for i in range(len(graph)) if graph[vertex][i] == 1]
    return res

def ham_cycle(graph):
    def completed(part):
        if len(part) == len(graph):# and graph[part[-1]][0]:
            return True

    def options(part):
        res = []
        path = [0] + part
        for v in neighbour(path[-1], graph):
            if v not in path:
                res += [v]
        return res

    res = solutions(completed, options)
    return res

graph = [[0, 1, 0, 1, 0], 
        [1, 0, 1, 1, 1], 
        [0, 1, 0, 0, 1], 
        [1, 1, 0, 0, 1], 
        [0, 1, 1, 1, 0]]



def nqueengen(n):
    def completed(part):
        if len(part) == n:
            return [part]

    def options(part):
        res = []
        col = len(part)
        for row in range(n):
            if not is_atk(row, col, part):
                res += [row]
        return res

    res = solutions(completed, options)
    return res

def quiz_total(q1, q2 ,q3, q4, q5):
    scores = [q1, q2, q3, q4, q5]
    return sum(scores) / len(scores)

def ass_total(a1, a2, a3, a4, a5):
    scores = [a1, a2, a3, a4, a5]
    return sum(scores) / len(scores)

quiz = quiz_total(11/15, 8/15, 6/15, 1/15, 11/15) * 0.15
ass = ass_total(12/20, 10/20, 19/20, 14/20, 16/20) * 0.20
attendence = 0.05
def overall(quiz, assignment, attendence):
    lst = [quiz, assignment, attendence]
    return sum(lst) / 0.40 * 100

print(overall(quiz, ass, attendence))


def emma_gay_camel(fuck):
    return fuck

fuck = "emma ghey"

print(emma_gay_camel(fuck))
