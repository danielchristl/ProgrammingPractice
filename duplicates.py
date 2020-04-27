#algorithm that removes duplicates from an array in place.
# Initial thought: sort array using algorithm that sorts in place (insertion sort), then
# manually go through and remove all duplicates
from InsertionSort import insertionSort
def remove_duplicates(arry):
    # worst case: O(n**2)
    sortedArry = insertionSort(arry)
    i = 0
    # O(n)
    while i + 1 < len(sortedArry):
        if sortedArry[i] == sortedArry[i + 1]:
            del sortedArry[i + 1]
            i -= 1
        i += 1
    return sortedArry
#
# print(remove_duplicates([1, 1, 2, 2, 3, 3]))
# print(remove_duplicates([4, 5, 6, 4, 5, 5]))
# print(remove_duplicates([]))
# print(remove_duplicates([0, 0, 0, 0, 0, 0, 0]))
# print(remove_duplicates([9, 8, 7, 6, 5]))
# print(remove_duplicates([9, 8, 9, 3, 4, 5, 6,4,4,234,2,45,6,2,1,5,46,6,4,3,8,8,6,1,5,24,3,7,89,7,1,2,3,5,8,3,7,4,5]))
