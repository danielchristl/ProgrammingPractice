def frequencyAndIndex(givenString):
    freqDict = {}

    # Returns a dictionary where the first entry is the frequency and the
    # second the first index of occurence
    for index, letter in enumerate(givenString.lower()):
        if letter not in freqDict:
            freqDict[letter] = (1, index)
        else:
            freqDict[letter] = (freqDict[letter][0] + 1, freqDict[letter][1])
    return freqDict
# print(frequencyAndIndex("Hello World"))


def firstNoRepeatChar(givenString):
    # If there are no characters
    if len(givenString) == 0:
        return "String given is empty"

    givenString = givenString.lower()
    # Return the frequency and index of each of the characters in the string
    freqDict = frequencyAndIndex(givenString)


    # List storing a tuple of all characters that appeared only once and their index of appearance
    firstAppearances = []
    for key, value in freqDict.items():
        if value[0] == 1:
            firstAppearances.append((value[1], key))

    # If every character repeats
    if len(firstAppearances) == 0:
        return "No entry appears without repeating"

    # Return the entry that appeared first within the firstAppearances list
    return min(firstAppearances)[1]


print(firstNoRepeatChar(""))
print(firstNoRepeatChar("aa"))
print(firstNoRepeatChar("hello world"))
print(firstNoRepeatChar("Hello World"))



# def frequency(givenString):
#     freqDict = {}
#     for letter in givenString.lower():
#         if letter not in freqDict:
#             freqDict[letter] = 1
#         else:
#             freqDict[letter] += 1
#     return freqDict
# print(frequency("Hello World"))

