def kcals(kcalLookup, ingredients):
    total = 0
    for ingredient in ingredients:
        (amount, type) = ingredient # This is called pattern matching. More readable than indexing: ingredient[0]
        total += amount * kcalLookup[type]
    return total