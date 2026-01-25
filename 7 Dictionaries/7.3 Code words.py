def code_words(text, dictionary):
    words = text.split(" ")
    newWords = []
    for word in words:
        # Get the code word for the word, otherwise return the original word
        word = dictionary.get(word, word)
        newWords.append(word)
    return " ".join(newWords) # Could make this more efficient with a counter, so we don't get duplicate list (words and newWords)