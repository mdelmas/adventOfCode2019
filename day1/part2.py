import math

def calculateFuelRequirement(modulesMasses):
    totalFuelRequirement = 0
    for moduleMass in modulesMasses:
        fuelRequirement = math.floor(moduleMass/3) - 2
        while fuelRequirement > 0:
            totalFuelRequirement += fuelRequirement
            fuelRequirement = math.floor(fuelRequirement/3) - 2
    return totalFuelRequirement

modulesMasses = [int(line.strip()) for line in open("./input")]
totalFuelRequirement = calculateFuelRequirement(modulesMasses)
print("Fuel requirement is " + str(totalFuelRequirement))
