def quick(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()

    smaller = []
    greater = []

    for each in arr:
        if each < pivot:
            smaller.append(each)
        else:
            greater.append(each)
    
    return quick(smaller) + [pivot] + quick(greater)



print(quick([4,2,6,1,3,7,4,7,8,4,5,8,3]))

# Time complexity best case = O(nlogn)
# Time complexity worst case = O(n^2)