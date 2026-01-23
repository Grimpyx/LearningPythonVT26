import collections.abc

def find_subsequence(sub,seq):
    # To check if seq is a generator or a sequence we can use a library
    # called collections. Searching around this seemed like a nice way to do it.
    if isinstance(seq, collections.abc.Sequence): seq = iter(seq)

    counter = 0
    comparisonList = []
    
    # Initial populating of the comparison list.
    for element in sub: 
        nextVal = next(seq, False)
        if nextVal == False: return # Stops this method when we've reached the end of the sequence
        comparisonList.append(nextVal)
        
    # We're not allowed to convert seq to a list, because that would be an infinite number of values.
    # However, we're able to populate a list with the first few values and then compare them to our
    # subsequence. If our subsequence has length 5, we populate comparisonList with the first 5 values
    # from the generator function. If sub and comparisonList is an exact match, we yield the current counter.
    # At the end we append the next value in seq and remove the first one. We compare, then repeat.
    # For example:
    # seq = "SRPSRPRPSSRRPPPPR"
    # sub = "RPS"
    # Iteration 0: comparisonList starts out as "SRP". Doesn't match with "RPS".
    # Iteration 1: comparisonlist becomes "SRPS", then first element is removed to "RPS". Matches with "RPS". We yield the counter, giving us the index.
    while True:
        check = True # becomes false if any element doesn't match
        for subCounter in range(0, len(sub)):
            if sub[subCounter] != comparisonList[subCounter]:
                check = False
                break
        if check: yield counter
        counter += 1

        # Prepares for thenxt iteration.
        nextVal = next(seq, False) # Get next value from seq. False is the default if we've reached the end of the sequence.
        if nextVal == False: return # Stops this method when we've reached the end of the sequence
        comparisonList.append(nextVal)
        comparisonList = comparisonList[1:] # Slice the list to remove the first element


# Works only for sequences that are not generators. This was my first attempt
def find_subsequence_NOTgenerator(sub,seq):
    for startIndex in range(0, len(seq) - len(sub)):
        check = True
        for nextIndex in range(0, len(sub)):
            if seq[startIndex + nextIndex] != sub[nextIndex]:
                check = False
                break
        if check: yield startIndex

# Tests the given example in the assignment
for element in find_subsequence("RP", iter("SRPSRPRPSSRRPPPPRR")):
    print(element)