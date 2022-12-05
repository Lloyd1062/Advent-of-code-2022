#PART 1
with open("input.txt") as f:
    allSacks = f.read().split("\n")
    duplicates = []
    for sack in allSacks:
        midIndex = len(sack)//2
        firstCompartment = sack[:midIndex]
        secondCompartment = sack[midIndex:]
        sameLet = ''
        for char in firstCompartment:
            for cringe in secondCompartment:
                if char == cringe:
                    sameLet += char
        if len(sameLet) > 0:
            duplicates.append(sameLet[0])            

    priorities = [ord(x)-96 if x.islower() else ord(x)-38 for x in duplicates]
    print(sum(priorities))
    f.close()

#PART 2
with open("input.txt") as f:
    allSacks = f.read().split("\n")
    groups = [[allSacks[k], allSacks[k+1], allSacks[k+2]] for k in range(0, len(allSacks), 3)]
    duplicates = []
    for group in groups:
        dupe = ''
        for x in group[0]:
            for y in group[1]:
                for z in group[2]:
                    if x == y == z:
                        dupe += x
        if len(dupe) > 0:
            duplicates.append(dupe[0])
    priorities = [ord(x)-96 if x.islower() else ord(x)-38 for x in duplicates]
    print(sum(priorities))