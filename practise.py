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
import random
test = random.sample(range(0, 100), 10)
def rSelSort(lst):
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

print(empty_graph(3))
