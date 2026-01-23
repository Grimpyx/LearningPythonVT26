def caesar(n, word):
    # Note: .split doesnt work when we dont use a separator. using constructor for the class list instead
    # The below line translates to "in the list converted word, for each char shift it by n and then join all of them into one string"
    return "".join(shiftLetter(n,c) for c in list(word))

# Shifts the letter. Adapts if the char is uppercase.
def shiftLetter(n, char):
    isUppercase = char == char.upper() # remember if it was upper case
    if isUppercase: char = char.lower() # ensure it's lower case. Essential for wrapping logic below.

    nr = ord(char) + n # shift letter by n

    # Correct by wrapping left or right
    if nr > 122: nr -= 26  # wrap around if after z
    elif nr < 97: nr += 26 # wrap around if before a

    # Converts back to character, and then corrects for upper case (although testing logic doesn't test for upper casee)
    char = chr(nr)
    if isUppercase: char = char.upper() # convert back to upper case

    return char

print(caesar(2,'secret'))