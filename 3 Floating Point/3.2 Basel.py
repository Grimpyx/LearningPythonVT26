import math

# returns an approximation of the Basel sum
# epsilon measures "how close" we are to the converging sum
def basel(epsilon):
    sum = 0
    counter = 1

    # Idea: add terms until the change is negligible
    while True:
        nextTerm = 1/math.pow(counter,2)
        counter += 1

        if nextTerm < epsilon:
            break
        else: sum += nextTerm
    return sum
