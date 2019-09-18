#Kathryn Marini 9/17/19
def gasolineGallons():
    gallons = float(input("Number of gallons of gasoline:"))
    liters = float(gallons * 3.785411784)
    barrelsOfOil = float(gallons / 19.5)
    poundsOfCO2 = float(gallons * 20)
    price = float(gallons * 3.35)
    print("number of liters ",liters)
    print("number of barrels of oil required to make this amount of gasoline ",barrelsOfOil)
    print("number of pounds of CO2 produced ",poundsOfCO2)
    print("price in US dollars ",price)
gasolineGallons()
                  
