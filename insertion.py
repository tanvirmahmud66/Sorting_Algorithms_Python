def insertion(arr):
    for i in range(1, len(arr)):
        current = arr[i]

        while arr[i-1]>current and i>0:
            arr[i-1], arr[i] = arr[i],arr[i-1]
            i-=1



arr = [2,6,1,3,7,7,4,9]
print("Unsorted Array: ", arr)
insertion(arr)
print("Sorted Array: ",arr)

# time complexity = O(n^2)