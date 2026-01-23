def acronym(s):
    words = s.split(" ") # Split string by white space, aka spacebar
    acronym = "".join(word[0] for word in words) # Short hand way of doing "for each word in words, select its first letter"
    return acronym.upper() # All uppercase

print(acronym("din mamma på pizza"))