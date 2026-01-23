def numeric_value(string):
    sum = 0
    for char in string.lower():
        sum += ord(char)-96
    return sum

print(numeric_value("Alice")) # gives 30