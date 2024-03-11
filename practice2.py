# ----------------------- selection sort
def selection_sort(arr):
    size  = len(arr)
    for i in range(size-1):
        mini = i
        for j in range(i+1, size):
            if arr[j]<arr[mini]:
                mini = j
        arr[i],arr[mini] = arr[mini],arr[i]


# ----------------------- bubble sort
def bubble_sort(arr):
    size  = len(arr)
    for i in range(size):
        for j in range(size-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]


# ----------------------- insertion sort
def insertion_sort(arr):
    size = len(arr)
    for i in range(1, size):
        while arr[i-1]>arr[i] and i>0:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1


# ----------------------- merge sort
def merge(left, right):
    new = []
    i,j = 0,0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
    new += left[i:]
    new += right[j:]
    return new

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    left_array = arr[:mid]
    right_array = arr[mid:]

    left_array = merge_sort(left_array)
    right_array = merge_sort(right_array)
    
    return merge(left_array, right_array)


# ----------------------- quick sort
def quick_sort(arr):
    length = len(arr)
    if length<=1:
        return arr
    else:
        pivot = arr.pop()

    smaller = []
    greater = []

    for each in arr:
        if each<pivot:
            smaller.append(each)
        else:
            greater.append(each)
    
    return quick_sort(smaller) + [pivot] + quick_sort(greater)



#------------------------ Driven code
arr = [2,525,67,7,3,7,78,3,7,4578,8,34,3442,7,78,474]
# selection_sort(arr)
# bubble_sort(arr)
# insertion_sort(arr)
# print("sorted array: ", arr)
# print("sorted array: ", merge_sort(arr))
print("sorted array: ", quick_sort(arr))