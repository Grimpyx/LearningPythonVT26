def cube_root(r,epsilon):
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

cube_root(123456, 0.001)