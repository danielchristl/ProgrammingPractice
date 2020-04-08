def bubbleSort(array):
    # Initialize array to be unsorted
    notFinished = True
    while (notFinished):
        # Array is potentially sorted
        notFinished = False
        # Go until the second to last element
        for index in range(len(array) - 1):
            # Swap if two elements are out of order
            if (array[index] > array[index + 1]):
                # Simple swap operation
                temp = array[index]
                array[index] = array[index + 1]
                array[index + 1] = temp
                # Potentially unsorted, need another pass
                notFinished = True
    return array

print(bubbleSort([2, 1, 3])) # PASSED
print(bubbleSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # PASSED
print(bubbleSort([])) # PASSED
print(bubbleSort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # PASSED
print(bubbleSort([2, 1, 1, 1, 3, 1, 1, 2])) # PASSED

# Analysis: My algorithm can be optimized by not passing through elements that are already sorted. This would
# be done by going from (0, n - 1), (0, n - 2), ..., (0, n - (n - 1)) where n is the length of the array

# Runtime: Bubble sort is average case and worst case O(n**2) because it goest through (n)(n - 1)/2 iterations.
# It is best case O(n) when the array is sorted because it only needs to make one pass.
