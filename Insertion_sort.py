def insertionSort(arr):
	# Get the length of the array
	n = len(arr)  
	# return the array if it has 0 or 1 element
	if n <= 1:
		return  
    # start iterating from second element
	for i in range(1, n): 
		#store the current element as key
		key = arr[i]  
		j = i-1
		#move elements which are greater ahead
		while j >= 0 and key < arr[j]:
			 # Shift elements to the right  
			arr[j+1] = arr[j] 
			j -= 1
		# Insert the key in the correct position
		arr[j+1] = key  

# Sort the array  
arr = [17,2,5,19,23]
insertionSort(arr)
print("The array after insertion sort is:",arr)
