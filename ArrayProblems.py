import random

# How do you find the missing number in a given integer array of 1 to 100?
# O(n)
def findMissingNumber(array):
    sumTo100 = int((99 * 100)/2) # Originally sum(range(100))
    sumArray = sum(array)
    missingNumber = sumTo100 - sumArray
    if missingNumber < 0 or missingNumber > 99:
        print("Invalid array received")
    return missingNumber
def testFindMissingNumber():
    for i in range(100):
        randomNumber = random.randrange(0, 99)
        array = list(range(0, 100))
        random.shuffle(array)
        array.remove(randomNumber)
        numberFound = findMissingNumber(array)
        if numberFound != randomNumber:
            print("findMissingNumber Failed. Expected number was " + str(randomNumber) +
                  " number found was " + str(numberFound))
            return
    print("Success! findMissingNumber passed")
    return
testFindMissingNumber()
# How do you find the duplicate number on a given integer array?
#O(n)
def duplicateNumber(array):
    duplicateDict = {}
    for i in array:
        if i not in duplicateDict:
            duplicateDict[i] = True
        else:
            return i
    return -1

def testDuplicateNumber():
    for i in range(100):
        randomNumber = random.randrange(0, 99)
        array = list(range(0, 100))
        array.append(randomNumber)
        random.shuffle(array)
        numberFound = duplicateNumber(array)
        if numberFound != randomNumber:
            print("duplicateNumber Failed. Expected number was " + str(randomNumber) +
                  " number found was " + str(numberFound))
            return
    print("Success! duplicateNumber passed")
    return
testDuplicateNumber()
# How do you find the largest and smallest number in an unsorted integer array?
# this is really easy, just store global max/min and compare at each step iterating through the array.
# Done this too many times already


# How do you find all pairs of an integer array whose sum is equal to a given number?

# How do you find duplicate numbers in an array if it contains multiple duplicates?
# How are duplicates removed from a given array in Java?
# How is an integer array sorted in place using the quicksort algorithm?
# How do you remove duplicates from an array in place?
# How do you reverse an array in place in Java?
# How are duplicates removed from an array without using any library?
