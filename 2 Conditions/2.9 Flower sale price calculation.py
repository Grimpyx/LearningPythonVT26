pricePerFlower = 20

def calculate_flower_price(flower_count, week_number):
    basePrice = flower_count * pricePerFlower
    twoForOnePrice = basePrice + 1 # vvvv
    bulkPrice = basePrice + 1 # For the function min() I need the starting price of the discounts to be more expensive than the base price

    if (14 <= week_number <= 17):
        if (flower_count % 2 == 1): # if is odd
            twoForOnePrice = pricePerFlower + pricePerFlower * (flower_count - 1) / 2
        else: twoForOnePrice = pricePerFlower * flower_count / 2
    if (flower_count >= 200):
        bulkPrice = basePrice * 0.8
        
    minimum = min([basePrice, twoForOnePrice, bulkPrice])
    return int(minimum) # rounds/truncate 60.0 to 60, 4000.0 to 4000


def main():
    # read input data
    nrFlowers = int(input("Enter the number of flowers: "))
    nrWeek = int(input("Enter the week number: "))

    # use calculate_flower_price to do the computation
    result = calculate_flower_price(nrFlowers, nrWeek)

    # print the result
    print(f"The price is {result}")