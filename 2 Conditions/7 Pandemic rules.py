# numC: the infection rate in Country C (given as a rate per 100_000)
# totalNum: the number of cases for two weeks in the traveler's country
# population: the population of the traveler's country.
def pandemic_rules(numC, totalNum, population):
    travelerC = (totalNum/population)*100_000
    if travelerC < 25 or travelerC < numC: return "green"
    elif 25 <= travelerC < 50: return "yellow"
    else: return "red"
    #elif travelerC >= 50: return "red"
