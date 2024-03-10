
def merge(left, right):
    new = []
    i,j = 0,0

    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
        
    new.extend(left[i:])
    new.extend(right[j:])
    return new


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left_array = arr[:mid]
    right_array = arr[mid:]

    l_array = merge_sort(left_array)
    r_array = merge_sort(right_array)

    return merge(l_array, r_array)



arr = [2,5,1,2,6,42,56,22,66,74,26,16,38,82,7,2,33]
print("Unsorted Array: ",arr)
print("Sorted Array: ", merge_sort(arr))


# time complexity = O(nlogn)
