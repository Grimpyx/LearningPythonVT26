def movieTickets(nrTickets, nrUnder18, time):
    price = nrTickets * 100
    price -= nrUnder18 * 50
    if time < 18: price *= 0.9 # hell yeah inline if statements
    return price