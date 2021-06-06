#part 1
#q1
# a - b ** c / b

#q2
#start = i1, j1, end = i2, j2
def check_overlap(i1, i2, j1, j2):
    for n in range(i1, i2 + 1):
        for k in range(j1, j2 + 1):
            if n == k:
                return False
    return True

#q3
def king_atk(c1, r1, c2, r2):
    cdiff = abs(c1 - c2)
    rdiff = abs(r1 - r2)
    if cdiff == 0:
        if rdiff == 1:
            return True
    elif cdiff == 1:
        if rdiff == 0:
            return True
        elif rdiff == 1:
            return True
    return False

#q4
def is_suffix(a, b):
    n1 = len(a)
    n2 = len(b)
    counter = 0
    if n1 > n2:
        return False
    for i in b[n2 - n1:]:
        if i == a[counter]:
            counter += 1
        else:
            return False
    return True

#q5
#[2, 3, 10, 4, 6, 7]
#[2, 3, 10, 4, 6, 7]
#[2, 3, 4, 10, 6, 7]
#[2, 3, 4, 6, 10, 7]
#[2, 3, 4, 6, 7, 10]

#q6
#Add adjacent vertices to boundary then pop() last entry and repeat

#q7
#[{2, 3, 5, 7, 7, 12, 15, 18, 26, 27, 50}]
#[{2, 3, 5, 7, 7}]
#[{5, 7, 7}]
#[7] (index 4)

#q8
#O(n ** 2)

#q9
#O(n)

#q10
#O(log(n))

#q11
#O(nlog(n))

#q12
#[[0, 1, 1, 1000],
#[1, 0, 1, 10],
#[1, 1, 0, 1],
#[1000, 10, 1, 0]]