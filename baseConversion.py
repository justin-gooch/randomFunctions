def baseConversion(originBase, numArray, newBase):
    numArray = numArray[::-1]
    number = 0
    for x in range(0, len(numArray)):
        number += numArray[x]*originBase**x
    numArray = []
    powerOf = 0
    while newBase**powerOf < number:
        powerOf += 1
    for x in range(powerOf-1, -1, -1):
        numArray.append(number/newBase**x)
        number = number%newBase**x
    return numArray
bc = baseConversion(26, [1,2,3,4], 5)
