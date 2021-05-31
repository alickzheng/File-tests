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

print(lex_suc([6, 7, 5, 1], [10, 7, 6, 1]))

def lex_pred(bitlst):
    res = bitlst[:]
    i = len(res) - 1
    while res[i] == 0:
        res[i] = 1
        i -= 1
    res[i] = 0
    return res