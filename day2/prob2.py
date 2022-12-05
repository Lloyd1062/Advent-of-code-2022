#A = Rock, B = Paper, C = Scissors
#XYZ
#1 = Rock, 2, 3
#0 = Loss, 3 = Draw, 6 = Win

with open("input.txt", "r") as f:
    values = {
        "X" : 1,
        "Y" : 2,
        "Z" : 3
    }
    winLossTie = {
        "X" : 0,
        "Y" : 3,
        "Z" : 6
    }
    choose = {
        "A X" : "Z",
        "A Y" : "X",
        "A Z" : "Y",
        "B X" : "X",
        "B Y" : "Y",
        "B Z" : "Z",
        "C X" : "Y",
        "C Y" : "Z",
        "C Z" : "X"
    }


    score = 0
    lines = f.read().split("\n")
    for i in range(len(lines)):
        line = lines[i]
        chars = choose[line]
        shape = values[chars]
        win = winLossTie[(line.split(" "))[1]]
        score += shape + win

    print(score)


