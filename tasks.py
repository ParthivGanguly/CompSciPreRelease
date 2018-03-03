# TASK 1

YIELDTHRESHOLD = 12.0
DAYSOFWEEK = 4
CowPopulation = 0
while CowPopulation <= 0 or CowPopulation > 999:
    try:
        CowPopulation = int(input("Enter number of cows in the herd: "))
    except ValueError:
        print("Please type a number, not alphabets")
    if CowPopulation <= 0 or CowPopulation > 999:
        print("Cow Population must be between 1 to 999 (inclusive)")
yields = []
for i in range(CowPopulation):
    yields.append([])
for day in range(1, 8):
    NumTimesCowYielded = []
    for i in range(CowPopulation):
        NumTimesCowYielded.append(0)
    print("Day " + str(day))
    CowMilkTime = 0
    while True:
        CowMilkTime += 1
        cowID = ""
        stop = False
        while not stop:
            cowID = input("Enter Cow ID: ")
            if len(cowID) < 3 or len(cowID) > 3:
                print("Cow ID must be exactly 3 digits long")
                stop = False
            else:
                stop = True
            CowsRegistered = 0
            cowIDPresent = False
            for cow in yields:
                if cow != [] and cow[0] == str(cow[0]):
                    CowsRegistered += 1
                    if cowID in cow:
                        cowIDPresent = True
            if CowsRegistered == CowPopulation and not cowIDPresent:
                print("Cow ID not part of the herd")
                stop = False
            else:
                stop = True
            for cow in yields:
                if cowID in cow:
                    if NumTimesCowYielded[yields.index(cow)] >= 2:
                        print("You can milk the cow twice at a maximum")
                        stop = False
                    else:
                        stop = True
                    break
        litres = 0.0
        while litres <= 0.0:
            litres = round(float(input("Enter litres of milk: ")), 1)
            if litres <= 0.0:
                print("Enter positive number")
        for cow in yields:
            if cowID in cow:
                if len(cow) == day:
                    cow.append(litres)
                else:
                    cow[day] += litres
                NumTimesCowYielded[yields.index(cow)] += 1
                break
            elif len(cow) == 0:
                cow.append(cowID)
                if day != 1:
                    for i in range(day - 1):
                        cow.append(0.0)
                cow.append(litres)
                NumTimesCowYielded[yields.index(cow)] += 1
                break
        if CowMilkTime == 2 * CowPopulation:
            break
        if input("Are all the cows done ? Yes (y) or No (Any other key): ") == "y":
            for cow in yields:
                if len(cow) <= day and len(cow) != 0:
                    cow.append(0.0)
            break

# TASK 2

TotalMilk = 0
for cow in yields:
    for milk in cow:
        if str(milk) != milk:
            TotalMilk += milk
print("Average volume of milk per cow: " + str(round(TotalMilk / CowPopulation, 0)))
print("Total weekly volume of milk: " + str(round(TotalMilk, 0)))

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
print("The cow that gave the highest milk volume is cow " + BestCow + " who gave " + str(max(TotalMilk)))
for cow in BadCows:
    print("Cow " + cow + " gave less than " + str(YIELDTHRESHOLD) + " litres for " + str(DAYSOFWEEK) + " or more days")
