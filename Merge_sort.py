def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle of the array
        mid = len(arr) // 2
        
        # Dividing the array into half
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        #sort the array recursively
        merge_sort(left_half)
        merge_sort(right_half)
        
         
        i = j = k = 0
        
        # Merge the two halves 
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Copy elements from left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Copy elements from right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

 
arr = [12, 11, 13, 5, 6, 7]

print("Original array:", arr)
merge_sort(arr)
print(" The array after merge sort is:", arr)
