def word_index(sentence):
    wordLookup = {} # empty dictionary
    words = sentence.split(" ")

    index = 0
    for word in words:
        if word == '': continue
        # Get the list of occurances.
        # If the word has no occurances yet, we give it an empty list.
        # Then we append the current word index
        wordLookup.setdefault(word, []).append(index)
        index += 1
    return wordLookup

# Test run:
print(word_index('the spider indexes the spider web'))