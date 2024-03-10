def Selection(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        arr[i],arr[mini] = arr[mini],arr[i]


arr = [20,5,2,6,3,6,23,67,23,34,26,36,67,43,4]
print("Unsorted Array: ", arr)
Selection(arr)
print("Sorted Array: ",arr)


# time complexity = O(n^2)