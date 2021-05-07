def merge(lst1, lst2):
    res = []
    n1, n2 = len(lst1), len(lst2)
    i, j = 0, 0
    while i < n1 and j < n2:
        if lst1[i] <= lst2[j]:
            res += [lst1[i]]
            i += 1
        else:
            res += [lst2[j]]
            j += 1
    return res + lst1[i:] + lst2[j:]

def mergesort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    else:
        sub1 = mergesort(lst[:n//2])
        sub2 = mergesort(lst[n//2:])
        return merge(sub1, sub2)

def strtolst(string):
    n = len(string)
    res = [[] for _ in range(n)]
    for i in range(n):
        res[i] = string[i]
    return res

def mergesort_iterative(ls):
    k, n = 1, len(ls)
    while k < n:
        nxt = []
        for a in range(0, n, 2*k):
            b, c = a + k, a + 2*k
            nxt += merge(ls[a:b], ls[b:c])
        ls = nxt
        print(ls)
        k = 2 * k
    return ls

'''
def block_count(string):
    if len(string) <= 1:
        return 1
    n = 0
    check = []
    if string[0] == string[1]:
        check.append(string[0])
    else:
        n += 1
    return n + block_count(string[1:])

print(block_count("CCDDDDDDDDC"))

def block_count(string):
    if len(string) <= 1:
        return 1
    n = 0
    if string[0] != string[1]:
        n += 1
    return n + block_count(string[1:])
print(block_count("AABBCCCBBDDD"))
'''


def mean_grade(stud_id, results):
    sum_grades = 0
    n = 0
    for i in results:
        if i[1] == stud_id:
            sum_grades += i[2]
            n += 1
    return sum_grades/n

results = [['Database', 101028, 65], 
['Database', 101022, 80],
['Operating Systems', 493968, 68],
['Operating Systems', 201022, 59],
['Java Fundamentals', 493968, 45],
['Java Fundamentals', 101022, 85],
['Mathematics', 101022, 71],
['Mathematics', 493968, 67],
['Information Systems', 493968, 75]]

import math
x = [1, 1]
y = [2, 5]
eucdif = math.sqrt(pow(x[0]-x[1],2)+pow(y[0]-y[1],2))
print(eucdif)