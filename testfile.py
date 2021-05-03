import random
randomlist = []
for i in range(0,10):
    n = random.randint(1,10)
    randomlist.append(n)
print(randomlist)

def merge(lst):
    if len(lst) > 1:
        #find middle index of the array rounded down
        mid = len(lst)//2
        #the list from 0 to mid
        leftlst = lst[:mid]
        #the list from mid to end of list
        rightlst = lst[mid:]
        #run the merge custom function so it will keep splitting until the lists
        #are length of 1
        merge(leftlst)
        merge(rightlst)
        #index
        i = j = k = 0
    
        while i < len(leftlst) and j < len(rightlst):
            if leftlst[i] < rightlst[j]:
                lst[k] = leftlst[i]
                i += 1
            else :
                lst[k] = rightlst[j]
                j += 1
            k += 1
        
        while i < len(leftlst):
            lst[k] = leftlst[i]
            i += 1
            k += 1
        
        while j < len(rightlst):
            lst[k] = rightlst[j]
            j += 1
            k += 1
        return lst

print(merge(randomlist))