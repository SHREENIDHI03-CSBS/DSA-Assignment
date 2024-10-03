def selection_sort(arr):
    # Traverse through the array
    for i in range(len(arr)):
        # Find the minimum element  
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the minimum element with the first element of unsorted array
        arr[i], arr[min_index] = arr[min_index], arr[i]
 
arr = [ 56,22,88,45,99]

print("Original array:", arr)
selection_sort(arr)
print("The array after implementation of selection sort:", arr)
