# ----------------------------------- Selection sort
def selection(arr):
    n = len(arr)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini = j
        arr[i],arr[mini] = arr[mini], arr[i]

# ----------------------------------- Bubble sort
def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

# ----------------------------------- Insertion sort
def insertion(arr):
    n = len(arr)
    for i in range(1,n):
        current = arr[i]
        while arr[i-1]>current and i>0:
            arr[i-1], arr[i] = arr[i],arr[i-1]
            i -= 1

# ----------------------------------- Merge sort
def merge(left, right):
    new = []
    i,j = 0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
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




arr = [3,2,65,23,66,34,77,22,8,7,4,2,1]
print("Unsorted Array: ",arr)
# selection(arr)
# bubble(arr)
# insertion(arr)
print("Sorted Array: ", merge_sort(arr))
# print("Sorted Array: ",arr)