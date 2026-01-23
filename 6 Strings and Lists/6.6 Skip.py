def skip(n, list):
    returnList = []
    if n <= 0: return
    for i in range(0, len(list), n):
        returnList.append(list[i])
    return returnList

print(skip(2,['A','B','C','D','E']))
print(skip(3,[1,2,3,4,5,6,7]))