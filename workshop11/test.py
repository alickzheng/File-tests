test = [0, 1, 1]

def lex_suc(bitlst):
    res = bitlst[:]
    i = len(res) - 1
    while res[i] == 1:
        res[i] = 0
        i -= 1
    res[i] = 1
    return res

def lex_pred(bitlst):
    res = bitlst[:]
    i = len(res) - 1
    while res[i] == 0:
        res[i] = 1
        i -= 1
    res[i] = 0
    return res

def basebitlst(n):
    first = [0]*n
    last = [1]*n
    bitlst = [first]
    while bitlst[-1] != last:
        bitlst.append(lex_suc(bitlst[-1]))
    return bitlst

#def rbitlst(n):
#    if n == 0:
#        return [0]
#    else:
#        return [n] + rbitlst(n - 1)

def rbitlst(n):
    if n == 0:
        return []
    if n == 1:
        return [[0],[1]]
    if n == 2:
        return[[0, 0], [0, 1], [1, 0], [1, 1]]
    else:
        return [i.insert(0, 0) or i for i in rbitlst(n - 1)] + [j.insert(0, 1) or j for j in rbitlst(n - 1)]


def rpermutations(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        perm = []
        for i in lst:
            j = [x for x in lst if x != i]
            for p in rpermutations(j):
                perm.append([i]+p)
        return perm

def greedy_exchange(amount, denominations):
    """
    >>> greedy_exchange(56, [20, 10, 5, 1])
    [2, 1, 1, 1]
    >>> greedy_exchange(350, [100, 50, 10, 5, 2, 1])
    [3, 1, 0, 0, 0, 0]
    >>> greedy_exchange(12, [9, 6, 5, 1])
    [1, 0, 0, 3]
    """
    n = len(denominations)
    def score(i): return denominations[i]
    denominations_order = sorted(range(n), key=score, reverse=True)
    for i in range(n):
        denominations[i] = denominations[denominations_order[i]]
    selection = [0 for _ in range(n)]
    value = 0
    i = 0
    while value < amount:
        if denominations[i] + value <= amount:
            selection[i] += 1
            value += denominations[i]
        else:
            i += 1
    return selection, denominations_order

def lex_suc(bitlst, bounds):
    res = bitlst[:]
    n = len(res) - 1
    if bitlst == bounds:
        return bitlst
    while res[n] == bounds[n]:
        res[n] = 0
        n -= 1
    res[n] += 1
    return res

def bounded_lists(upper_bounds):
    n = len(upper_bounds)
    last = upper_bounds
    first = [0] * n
    res = [first]
    while res[-1] != last:
        res += [lex_suc(res[-1], upper_bounds)]
    return res

#print(lex_suc([1, 1, 2],[1, 1, 2]))
def brute_force_coin_exchange(amount, denominations):
    """
    Input: The target amount of you want to reach and a list of 
           coins (i.e. denominations) that you have an infinite amount of.
    Output: A list of integers where each index represents the number of 
            coins the denominations list.

    >>> brute_force_coin_exchange(15, [10, 7, 6, 1])
    [0, 2, 0, 1]
    """
    n = len(denominations)
    bounds = [0 for _ in range(n)]
    value = 0
    for i in range(n):
        value = 0
        while value + denominations[i] <= amount:
            value += denominations[i]
            bounds[i] += 1
    possible = bounded_lists(bounds)
    lst = []
    for i in possible:
        val = 0
        templst = [0 for _ in range(n)]
        for j in range(len(i)):
            val += denominations[j]*i[j]
            templst[j] = i[j]
        if val == 15:
            lst.append(templst)
    sumlst = []
    for i in lst:
        sumlst.append([sum(i)])
    used = sumlst.index(min(sumlst))
    return lst[used]

print(brute_force_coin_exchange(15, [10, 7, 6, 1]))