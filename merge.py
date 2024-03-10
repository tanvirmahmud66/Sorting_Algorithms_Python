def merge(left, right):
    new = []
    i,j = 0,0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j+=1
    new += left[i:]
    new += right[j:]
    return new


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_array = arr[:mid]
    right_array = arr[mid:]
    left_array = merge_sort(left_array)
    right_array = merge_sort(right_array)
    return merge(left_array, right_array)



arr = [23,52,62,62,46,23,62,64,7,7,7,2,35,67,2]
print("Unsorted Array: ", arr)
print("Sorted Array: ", merge_sort(arr))

# # time complexity = O(nlogn)