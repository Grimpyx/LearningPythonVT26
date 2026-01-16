import math

def guess_winner(white_rating, black_rating):
    score = 1/(1+math.pow(10,(black_rating-white_rating)/400))
    if score < 0.45: print("Black is expected to win")
    elif score > 0.55: print("White is expected to win")
    else: print("A draw is expected")