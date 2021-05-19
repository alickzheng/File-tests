def reverse(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse(lst[:-1])

def pair(lst):
    pair = []
    for i in lst:
        for j in range(len(lst)):
            if i != lst[j]:
                pair.append([i, lst[j]])
    return pair
check = pair("mathematics")
print(len(check))