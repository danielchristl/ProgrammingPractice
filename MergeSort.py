def merge(arry, left, middle, right):
    # Set up temporary arrays
    leftArray = arry[left : middle + 1]
    rightArray = arry[middle + 1 : right + 1]
    # Keep track of position in temporary arrays
    currLeft = 0
    currRight = 0
    # Keep track of position in overall array
    currPosition = left

    # While we still have comparisons to make/things are still possible our of order
    while currLeft < len(leftArray) and currRight < len(rightArray):

        # If the left array's element is greater, set the right element as the next element in overall array
        if leftArray[currLeft] > rightArray[currRight]:
            arry[currPosition] = rightArray[currRight]
            currRight += 1
        # Otherwise, set the left element as the next element in the overall array
        else:
            arry[currPosition] = leftArray[currLeft]
            currLeft += 1
        # Iterate through the overall array
        currPosition += 1

    # Once we reach this point, all the smaller numbers have been added to the overall array.
    # We must only add the sorted, greater numbers
    while currLeft < len(leftArray):
        arry[currPosition] = leftArray[currLeft]
        currLeft += 1
        currPosition += 1

    while currRight < len(rightArray):
        arry[currPosition] = rightArray[currRight]
        currRight += 1
        currPosition += 1

def mergeSort(arry, left, right):
    # Recurse until we can't divide the array anymore
    if (right > left):
        # Find middle point to divide the array at (integer division because Python does float division by default)
        middle = int((left + right)/2)
        # Recurse on first half, including middle
        mergeSort(arry, left, middle)
        # Recurse on second half, excluding middle
        mergeSort(arry, middle + 1, right)
        # Merge the sorted halves
        merge(arry, left, middle, right)
    return arry

# Simply insert array and leave the rest to mergesort
def runMergeSort(arry):
    return mergeSort(arry, 0, len(arry))

print(runMergeSort([1, 2, 3])) # PASSED
print(runMergeSort([2, 1, 3])) # PASSED
print(runMergeSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # PASSED
print(runMergeSort([])) # PASSED
print(runMergeSort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # PASSED
print(runMergeSort([2, 1, 1, 1, 3, 1, 1, 2])) # PASSED

# Analysis: Can be optimized in terms of space; if we do clever modulus and integer division, it is possible to
# run the merge portion of the algorithm in place. Thus, the algorithm would decrease from O(N) auxillary space to
# O(1) auxillary space.

# Runtime: Since there are 2 subproblems, the subproblems are reduced by 2 in each recursive call, and it takes f(n)
# at each level, we can conclude by Master Theorem that the runtime is O(nlog(n)).