# Function to perform bubble sort
def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through the array
    for i in range(n):
        # check for swapping
        swapped = False
        for j in range(0, n-i-1):
            # Swap with the next element if it is greater
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no two elements were swapped , it means the array is sorted
        if not swapped:
            break

arr = [99,55,44,33,88]

print("Original array:", arr)
bubble_sort(arr)
print("The array after implementation of bubble sort:", arr)
