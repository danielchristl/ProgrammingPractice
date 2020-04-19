# Operation for sorting whole numbers
def countingSort(arry):
    # O(n) time and space operation
    outputArray = arry.copy()
    # O(n) time operation
    maxNum = max(arry)
    # O(max(arry) time and space operation)
    countArray = [0] * (maxNum + 1)
    # O(n) time and space operation
    cumulativeArray = countArray.copy()
    # O(n) time operation
    for element in arry:
        countArray[element] += 1
    # O(n) time operation
    for index in range(maxNum + 1):
        if index == 0:
            cumulativeArray[index] = countArray[index]
        else:
            cumulativeArray[index] = cumulativeArray[index - 1] + countArray[index]
    #O(n) time operation
    print(cumulativeArray)
    for element in arry:
        outputArray[cumulativeArray[element] - 1] = element
        cumulativeArray[element] -= 1
    return outputArray

print(countingSort([10, 9, 8, 7, 6, 5, 4, 3, 5, 5, 5]))

# Analysis: This algorithm appears to be useful for highly repetitive arrays that consist only
# of whole numbers and where the max of the array is relatively small. This algorithm is
# O(max(input array)) in terms of both space and time complexity.
# Time complexity can be changed to O(len(arry) + range(arry)) with slight change in implementation.
