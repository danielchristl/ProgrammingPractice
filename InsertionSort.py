def insertionSort(arry):
    # Iterate through all elements
    for index in range(len(arry)):
        for subIndex in range(0, index):
            # if a number is smaller, resort the subarray
            if arry[index] < arry[subIndex]:
                temp = arry[index]
                while subIndex < index:
                    arry[index] = arry[index - 1]
                    index -= 1
                arry[subIndex] = temp
    return arry

print(insertionSort([2, 1, 3])) # PASSED
print(insertionSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # PASSED
print(insertionSort([])) # PASSED
print(insertionSort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # PASSED
print(insertionSort([2, 1, 1, 1, 3, 1, 1, 2])) # PASSED

# Analysis: My algorithm can be optimized by implementing binary search to replace the inner for loop.

# Runtime: Insertion sort is worst case O(n**2) because it can run as many as (n)(n-1)/2 times is the
# array is in reverse order. This algorithm sorts in place and thus takes O(1) auxillary space.
