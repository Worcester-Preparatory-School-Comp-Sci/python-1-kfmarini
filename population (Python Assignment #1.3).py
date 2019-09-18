#Kathryn Marini 9/17/19
def population():
    #This code calculates the estimated population with a user input for the year, using births, deaths, and immigrants summed up with the original population.
    years = float(input("How many years have passed?"))
    population = 307357870
    secondsToYears = 31536000
    births = years * secondsToYears * 7/60
    deaths = years * secondsToYears * 13/60
    immigrants = years * secondsToYears * 35/60
    newPopulation = population + births - deaths + immigrants
    print("Estimated population: ", newPopulation)
population()
