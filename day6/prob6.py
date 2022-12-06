input = "input.txt"

#PART 1
def unique(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)):
            if(str[i] == str[j]):
                return False
    return True

def partOne(input):
    with open(input, "r") as f:
        datastream = f.read()

        i = 0
        while i < len(datastream) - 4:
            potentialMarker = datastream[i:i+4]
            if unique(potentialMarker):
                return (i+4)
            i += 1


#PART 2

def partTwo(input):
    with open(input, "r") as f:
        datastream = f.read()
        i = 0
        while i < len(datastream) - 15:
            potentialMarker = datastream[i:i+14] 
            if unique(potentialMarker):
                return (i+14) #Note: datastream[i:i+14] is just datastream[i] + datastream[i+1] + ... + datastream[i+13] so we return i+14 to account for 0 indexing
            i += 1
        return ":("


print(f"PART 1: {partOne(input)}\nPART 2: {partTwo(input)}")