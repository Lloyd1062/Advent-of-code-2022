input = "input.txt"

#PART 1
def partOne(input):
    with open(input, "r") as f:
        file = f.read()
        directions = file.split("\n\n")[1].split("\n")
        Layout = {
            1 : "BVSNTCHQ",
            2 : "WDBG",
            3 : "FWRTSQB",
            4 : "LGWSZJDN",
            5 : "MPDVF",
            6 : "FWJ",
            7 : "LNQBJV",
            8 : "GTRCJQSN",
            9 : "JSQCWDM"
        }
        
        for direction in directions:
            moveX = int(direction.split(" ")[1])
            fromY = int(direction.split(" ")[3])
            toZ = int(direction.split(" ")[5])
            concat = Layout[fromY][-moveX:]
            Layout[fromY] = Layout[fromY][:-moveX]
            Layout[toZ] += concat[::-1]
        f.close()
    return "".join([Layout[1][-1], Layout[2][-1], Layout[3][-1], Layout[4][-1], Layout[5][-1], Layout[6][-1], Layout[7][-1], Layout[8][-1], Layout[9][-1]])
    
#PART 2
def partTwo(input):
    with open(input, "r") as f:
        file = f.read()
        directions = file.split("\n\n")[1].split("\n")
        Layout = {
            1 : "BVSNTCHQ",
            2 : "WDBG",
            3 : "FWRTSQB",
            4 : "LGWSZJDN",
            5 : "MPDVF",
            6 : "FWJ",
            7 : "LNQBJV",
            8 : "GTRCJQSN",
            9 : "JSQCWDM"
        }
        
        for direction in directions:
            moveX = int(direction.split(" ")[1])
            fromY = int(direction.split(" ")[3])
            toZ = int(direction.split(" ")[5])
            concat = Layout[fromY][-moveX:]
            Layout[fromY] = Layout[fromY][:-moveX]
            Layout[toZ] += concat #Only change is removing [::-1]
        f.close()
    return "".join([Layout[1][-1], Layout[2][-1], Layout[3][-1], Layout[4][-1], Layout[5][-1], Layout[6][-1], Layout[7][-1], Layout[8][-1], Layout[9][-1]])



print(f"PART 1: {partOne(input)}\nPART 2: {partTwo(input)}")