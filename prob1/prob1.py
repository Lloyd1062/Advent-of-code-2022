with open("input.txt", "r") as f:
    split = f.read().split("\n\n")
    good = []
    for i in range(len(split)):
        good.append(sum(map(int,split[i].split("\n"))))


good.sort(reverse=True)
print(sum([good[0], good[1], good[2]]))

