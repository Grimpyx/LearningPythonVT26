def find_numbers(n):
    for counter in range(0,n):
        calc = 12 * sum_of_digits(counter)
        if counter == calc: print(calc)

def sum_of_digits(x):
    return sum(int(digit) for digit in list(str(x)))

find_numbers(500000)