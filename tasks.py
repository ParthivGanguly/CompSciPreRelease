# TASK 1

YIELDTHRESHOLD = 12.0
DAYSOFWEEK = 4
CowPopulation = 0
while CowPopulation == 0 or CowPopulation > 999:
    CowPopulation = int(input("Enter number of cows in the herd: "))
    if CowPopulation == 0 or CowPopulation > 999:
        print("Cow Population must be between 1 to 999 (inclusive)")
yields = []
for i in range(CowPopulation):
    yields.append([])
for day in range(1, 8):
    dayOver = False
    while not dayOver:
        cowID = ""
        while len(cowID) > 3 or len(cowID) < 3:
            cowID = input("Enter Cow ID: ")
            if len(cowID) < 3 or len(cowID) > 3:
                print("Cow ID must be exactly 3 digits long")
        litres = 0.0
        while litres <= 0.0:
            litres = float(input("Enter litres of milk: "))
            if litres <= 0.0:
                print("Enter positive number")
        for cow in yields:
            if cowID in cow:
                if len(cow) == day:
                    cow.append(litres)
                else:
                    cow[day] += litres
            elif len(cow) == 0:
                cow.append(cowID)
                cow.append(litres)
                break
        if input("Is the day over ? Yes (y) or No (Any other key): ") == "y":
            for cow in yields:
                if len(cow) == day:
                    cow.append(0.0)
            dayOver = True

# TASK 2

TotalMilk = 0
for cow in yields:
    for milk in cow:
        if str(milk) != milk:
            TotalMilk += milk
print("Average volume of milk per cow: " + str(round(TotalMilk / CowPopulation, 0)))
print("Total weekly volume of milk: " + str(TotalMilk))

# TASK 3

TotalMilk = []
for cow in yields:
    CurrentCowMilk = 0
    for milk in cow:
        if str(milk) != milk:
            CurrentCowMilk += milk
    TotalMilk.append(CurrentCowMilk)
BestCow = yields[TotalMilk.index(max(TotalMilk))][0]
BadCows = []
for cow in yields:
    BadDays = 0
    for milk in cow:
        if str(milk) != milk and milk < YIELDTHRESHOLD:
            BadDays += 1
            if BadDays >= DAYSOFWEEK:
                BadCows.append(cow[0])
print("The cow that gave the highest milk volume is cow " + BestCow)
for cow in BadCows:
    print("Cow " + cow + " gave less than " + str(YIELDTHRESHOLD) + " litres for " + str(DAYSOFWEEK) + " or more days")
