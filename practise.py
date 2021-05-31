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

