# Returns the number of minimum swaps required to sort a consecutive array starting at 1 in O(n) time
# with O(n) auxiliary space.
def minSwaps(arr):
    numSwaps = 0
    visited = [False] * len(arr)
    i = 0
    j = 0
    while(j < len(arr)):
        if visited[i]:
            j += 1
            i = j
            continue
        # in a cycle
        if arr[i] - 1 != i:
            numSwaps += 1
            visited[i] = True
            i = arr[i] - 1
            # end cycle
            if visited[i]:
                numSwaps -= 1
        # number already in right place
        else:
            j += 1
            i = j

    return numSwaps