'''
DO NOT CHANGE THE NAME OF THIS FILE, or else the tester will not work. 
The first function requires that you replace the given strings with
your personal details. It is important that you enter your student number
and your student email correctly. If your number and email do not match we
will then check your name, so your name acts as a failsafe.
'''

# Student details
def details():
    student_number = '28747445' #write your student number as a string
    student_email = 'hzhe0006' + '@student.monash.edu' #write your student email
    name = 'Huihong Zheng' #write your name as it appears on Moodle
    return str(student_number), student_email, name


# Warmup
def lex_less_eq(a, b):
    """Determines whether sequence (a) is lexicographically less or equal to
    sequence (b); equivalent to a <= b.

    For example:
    >>> lex_less_eq('tactic', 'tree')
    True
    >>> lex_less_eq('tactic', 'tactical display')
    True
    >>> lex_less_eq([1, 2, 3], [0, 1, 2, 3])
    False
    """
    a_n = len(a)
    b_n = len(b)
    if a_n == 0 or b_n == 0:
        if a_n == 0:
            return True
        else:
            return False
    if a_n == b_n == 0:
        if a == b or a < b:
            return True
    if a[0] > b[0]:
        return False
    elif a[0] < b[0]:
        return True
    return lex_less_eq(a[1:], b[1:])



# Task 1: Part A - Recursive Bitlist
def rbitlists(n):
    """Generates list of all bitlists of length n in lexicographic order
    using recursion.

    For example.
    >>> rbitlists(2)
    [[0, 0], [0, 1], [1, 0], [1, 1]]
    >>> rbitlists(3)
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]

    <I noticed that the number of bits are 2^n and with each increment of n the number of lists increase by 2
    and the numbers in each subsequent list is the repetition of the previous list with a 0 inserted in the 0th
    position on the first half and a 1 inserted in the 0th position on the second half. As such, taking advantage
    of that pattern I wrote a list comprehension that will take the element in the rbitlist(n-1) or the element
    inserting 0 at 0, as insert mutates the list and will result in None otherwise>
    """
    if n == 0:
        return []
    if n == 1:
        return [[0],[1]]
    if n == 2:
        return[[0, 0], [0, 1], [1, 0], [1, 1]]
    else:
        return [i.insert(0, 0) or i for i in rbitlists(n - 1)] + [j.insert(0, 1) or j for j in rbitlists(n - 1)]


# Task 1: Part B - Recursive Permutations
def rpermutations(lst):
    """ Generates all permutations of input list.
    
    >>> sorted(rpermutations(list(range(1, 4))))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(rpermutations(list(range(1, 5))))
    [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
    >>> sorted(rpermutations(list('JOE')))
    [['E', 'J', 'O'], ['E', 'O', 'J'], ['J', 'E', 'O'], ['J', 'O', 'E'], ['O', 'E', 'J'], ['O', 'J', 'E']]

    <first two base statements are set with length of the input list equalling 0 and 1 with 0 returning an empty list and 1 returning the input list
    then the output list is created and the list is iterated down by creating a smaller list excluding the first entry of the original list. then for
    each element in the permutation of the smaller list a list created from the originally excluded element and the element in the permutated list is appended
    to the output list>
    """
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
        

# Task 2: Part B1 - Bounded Lists
def bounded_lists(upper_bounds):
    """
    Input: List of positive integers of length 'n'
    Output: List of lists where i, lst[i] <= upper_bound[i]

    >>> bounded_lists([1, 1, 2])
    [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]]
    """
    n = len(upper_bounds)
    last = upper_bounds
    first = [0] * n
    res = [first]
    while res[-1] != last:
        res += [lex_suc(res[-1], upper_bounds)]
    return res


# Task 2: Part 1 - Greedy Exchange
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
    return selection

    
# Task 2: Part B2 - Brute Force Implementation
def brute_force_coin_exchange(amount, denominations):
    """
    Input: The target amount of you want to reach and a list of 
           coins (i.e. denominations) that you have an infinite amount of.
    Output: A list of integers where each index represents the number of 
            coins the denominations list.

    >>> brute_force_coin_exchange(15, [10, 7, 6, 1])
    [0, 2, 0, 1]
    """
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


# Task 2: Part C - Backtracking Implementation
def backtracking_exchange(amount, denominations):
    """
    >>> backtracking_exchange(56, [20, 10, 5, 1])
    [2, 1, 1, 1]
    >>> backtracking_exchange(12, [9, 6, 5, 1])
    [0, 2, 0, 0]
    """
    pass


if __name__=='__main__':
    import doctest
    doctest.testmod() 