def swap(list):
    halfLength = int(len(list)/2)
    firstHalf = list[:halfLength]
    secondHalf = list[halfLength:]
    return secondHalf + firstHalf

print(swap([1,2,3,4]))