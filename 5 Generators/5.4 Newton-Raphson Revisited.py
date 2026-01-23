def cube_root_generator(r, initial_guess):
    guess = initial_guess
    while True:
        guess = (1/3)*(2*guess + r/(guess*guess))
        yield guess

def cube_root(r, epsilon): # Copied from assignment 3.6
    guess = 1.0
    counter = 0
    while True:
        print(f"Iteration {counter} : {guess}")
        nextGuess = (1/3)*(2*guess + r/(guess*guess))
        if abs(nextGuess - guess) < epsilon:
            return nextGuess
        else:
            guess = nextGuess
            counter += 1
            continue

# Used to test
def take_n(n, gen): # Copied from assignment 5.2
    counter = 0 # Used to terminate if we've extracted what we want
    returnList = []
    if isinstance(gen, range):
        gen = iter(gen) # Converts the range to a generator using iter()
    for item in gen: # similar to foreach loop in C#
        if counter >= n: break
        returnList.append(item)
        counter += 1
    return returnList

print(take_n(4, cube_root_generator(123456, 1.0)))