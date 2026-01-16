# prints amortization, interest, total
def calculate_loan(property_price,loan,interest_rate):
    ratio = loan/property_price
    amortization = 0
    if ratio >= 0.7: amortization = 0.02 * loan
    elif ratio >= 0.5: amortization = 0.01 * loan
    interest = loan * interest_rate / 100
    total = amortization + interest

    print(f"amortization: {int(amortization/12)}")
    print(f"interest: {int(interest/12)}")
    print(f"total: {int(total/12)}")

calculate_loan(15e5,6e5,1.2)