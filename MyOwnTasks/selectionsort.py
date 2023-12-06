def selectionsort(arr):
    smallest = arr[0]
    for i in range(0, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]    
    return smallest

print(selectionsort([5, 3, 6, 2, 10]))  
