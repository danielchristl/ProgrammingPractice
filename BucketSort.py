from InsertionSort import *


# Bucket sort is intended for floating point numbers from 0.0 to 1.0. When normally distributed,
# bucket sort sorts these numbers in O(n) average time
def bucketSort(arry):
    sortedArry = []
    bucketDict = {}
    for index in range(len(arry)):
        bucketDict[index] = []
    for element in arry:
        bucketDict[int(len(arry) * element)].append(element)
    for bucket in bucketDict:
        bucketDict[bucket] = insertionSort(bucketDict[bucket])
    for bucket in bucketDict:
        sortedArry.extend(bucketDict[bucket])
    return sortedArry

print(bucketSort([0.5, 0.2])) # PASSED
print(bucketSort([])) # PASSED
print(bucketSort([0.5, 0.3, 0.1])) # PASSED
print(bucketSort([0.2, 0.2, 0.2, 0.1])) # PASSED
print(bucketSort([0.1, 0.2, 0.3])) # PASSED
print(bucketSort([0.51231343534353, 0.22143213424312, 0.435345345, 0.957867, 0.412341234324, 0.1423454, 0.786786875, 0.53245234535324, 0.7848484768])) # PASSED
print(bucketSort([.20, .9, .8, .7, .6, .5, .4, .3, .2, .1])) # PASSED

