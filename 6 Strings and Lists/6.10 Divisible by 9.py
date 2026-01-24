# Assignment requires we print it out the sums as a list
def div9(num):
    if isinstance(num, str):
        num = int(num)
    
    listOfResults = [num]
    numberSum = num
    print(num)

    while numberSum >= 10:
        numAsString = str(listOfResults[-1])
        numberSum = sum(int(nr) for nr in list(numAsString)) # Separate all numbers (chars), convert to numbers, sum them
        listOfResults.append(numberSum)
        print(numberSum)
    
    return listOfResults

# Not used by assignment
def isDivisibleBy9(num):
    if isinstance(num, int):
        num = str(num)
    
    elements = list(num)
    numberSum = sum(int(nr) for nr in elements) # sum all numbers after they're converted with int()

    # This is a very ample case to use recursion (I think this is later in the course, but it's the same for all languages so I'll use it here)
    # The idea is to sum all numbers until we get a number under 10 (0 through 9)
    # At last we return true if sum is either 9 or 0.
    if (numberSum >= 10):
        return isDivisibleBy9(numberSum)
    else:
        return numberSum == 9 or numberSum == 0
    
print(div9(1998))
print(isDivisibleBy9(9))          # True
print(isDivisibleBy9(123))        # False
print(isDivisibleBy9(81))         # True
print(isDivisibleBy9(5555555))    # False
print(isDivisibleBy9(997002999))  # True
