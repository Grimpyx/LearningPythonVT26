def main():
    tries = int(input("Number of tries: "))
    conversions = int(input("Number of conversions: "))
    
    if conversions > tries: 
        print("Impossible: too many conversions or too few tries.")
        return

    penalties = int(input("Number of penalties: "))
    drop_goals = int(input("Number of drop_goals: "))
    
    tries *= 5
    conversions *= 2
    penalties *= 3
    drop_goals *= 3

    sum = tries + conversions + penalties + drop_goals

    print(f"Game points: {sum}") # "string formating"
    
    return

# Expected output in normal case for n game points: "Game points: n"
# Expected output in case of conversion error: "Impossible: too many conversions or too few tries."