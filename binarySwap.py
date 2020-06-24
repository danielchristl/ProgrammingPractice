# -*- coding: utf-8 -*-
"""
Program that takes an input in binary, reverses its bits, and converts it 
back to base 10
Why? Well, why not?
"""
def toBinary(posInt):
    binString = []
    if posInt == 0:
        return "0"
    while(posInt != 0):
        binString.insert(0, posInt%2)
        posInt = posInt//2
    binArray = ""
    for i in binString:
        binArray += str(i)
    return binArray

def pad(binary):
    newString = ""
    nearestEight = round(len(binary)/8 + .01)
    if len(binary) < 8:
        nearestEight = 1
    for i in range(8 * nearestEight - len(binary)):
        newString += '0'
    return newString + binary

def reverse(string):
    newString = ""
    length = len(string)
    for i in range(length):
        newString += string[length - i - 1]
    return newString

def toBase10(binary):
    returnNum = 0
    length = len(binary) - 1
    base = 0
    while(length >= 0):
        returnNum += int(binary[length]) * 2**base
        length -= 1
        base += 1
    return returnNum


def binaryReverse(posInt):
    posInt = int(posInt)
    # Make it binary
    binRep = toBinary(posInt)
    # Pad it
    padBinRep = pad(binRep)
    # Reverse it
    revPadBinRep = reverse(padBinRep)
    # Convert back to an integer
    return toBase10(revPadBinRep)

print(binaryReverse("4567"))
