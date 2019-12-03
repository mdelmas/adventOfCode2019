import math

def calculateFuelRequirement(modulesMasses):
    fuelRequirement = 0
    for moduleMass in modulesMasses:
        fuelRequirement += math.floor(moduleMass/3) - 2
    return fuelRequirement

modulesMasses = [int(line.strip()) for line in open("./input")]
fuelRequirement = calculateFuelRequirement(modulesMasses)
print("Fuel requirement is " + str(fuelRequirement))
