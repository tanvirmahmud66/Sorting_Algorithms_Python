def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()
    
    greater = []
    smaller = []

    for each in arr:
        if each < pivot:
            smaller.append(each)
        else:
            greater.append(each)
    
    return quick_sort(smaller) + [pivot] + quick_sort(greater)



print(quick_sort([3,5,65,1,6,2,6,7,2,7,7,7,2,7,8,2,4,7,8]))


# Time complexity best case = O(nlogn)
# Time complexity worst case = O(n^2)