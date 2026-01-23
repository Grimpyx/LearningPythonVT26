def take_n(n, gen):
    counter = 0 # Used to terminate if we've extracted what we want
    returnList = []
    if isinstance(gen, range):
        gen = iter(gen) # Converts the range to a generator using iter()
    for item in gen: # similar to foreach loop in C#
        if counter >= n: break
        returnList.append(item)
        counter += 1
    return returnList

# Clumsy way
#def take_n(n, gen):
    #returnList = []
    #if isinstance(gen, range): # Function needs to behave differently if gen happens to be a range. Range doesn't work with next()
        #r = range(0, min(n, gen.stop))
        #for i in r:
            #nextItem = i
            #returnList.append(nextItem)
    #else:
        #for i in range(0, n):
            #nextItem = next(gen)
            #returnList.append(nextItem)
    #return returnList

def testProgram():
    print("Testing: take_n(10, range(0,4))")
    print(take_n(10, range(0,4)))

    print("Testing: take_n(0, range(0,10))")
    print(take_n(0, range(0,10)))
testProgram()