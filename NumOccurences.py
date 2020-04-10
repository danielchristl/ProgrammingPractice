def occurences(givenString, char):
    count = 0
    for letter in givenString.lower():
        if letter.lower() == char:
            count += 1
    return count

print(occurences("Daniel Christl", 'c'))
print(occurences("Daniel Christl", 'i'))
# Runtime: O(n) (goes through entire string once)