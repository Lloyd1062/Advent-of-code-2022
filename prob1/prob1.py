with open("input.txt", "r") as f:
    split = f.read().split("\n\n")
    good = [sum(int(y) for y in x.split("\n")) for x in split]
    good.sort(reverse=True)
    print(sum([good[0], good[1], good[2]]))

#PART 2
