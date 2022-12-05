input = "input.txt"

#PART 1 Faster
def part1Faster(input): 
    with open(input) as f:
        allPairs = f.read().split("\n")
        answer = 0
        for pair in allPairs:
            pair1 = pair.split(",")[0]
            pair2 = pair.split(",")[1]
            pair1Range1 = int(pair1.split("-")[0])
            pair1Range2 = int(pair1.split("-")[1])
            pair2Range1 = int(pair2.split("-")[0])
            pair2Range2 = int(pair2.split("-")[1])

            if (pair2Range1 >= pair1Range1 and pair2Range2 <= pair1Range2) or (pair1Range1 >= pair2Range1 and pair1Range2 <= pair2Range2):
                answer += 1
        f.close()
    return(answer)

        
#PART 1 Less Code
def part1LessCode(input):
    with open(input) as f:
        allPairs = f.read().split("\n")
        answer = 0
        for pair in allPairs:
            pair1 = pair.split(",")[0]
            pair2 = pair.split(",")[1]
            pair1Range = range(int(pair1.split("-")[0]), int(pair1.split("-")[1])+1)
            pair2Range = range(int(pair2.split("-")[0]), int(pair2.split("-")[1])+1)
            if all(x in pair1Range for x in pair2Range) or all(x in pair2Range for x in pair1Range):
                answer += 1

        f.close()
    return answer


#PART 2 Haha it is literally just changing all to any
def part2(input):
    with open(input) as f:
        allPairs = f.read().split("\n")
        answer = 0
        for pair in allPairs:
            pair1 = pair.split(",")[0]
            pair2 = pair.split(",")[1]
            pair1Range = range(int(pair1.split("-")[0]), int(pair1.split("-")[1])+1)
            pair2Range = range(int(pair2.split("-")[0]), int(pair2.split("-")[1])+1)
            if any(x in pair1Range for x in pair2Range) or any(x in pair2Range for x in pair1Range):
                answer += 1

        f.close()
    return answer







print(f"PART 1: {part1LessCode(input)}")
print(f"PART 2: {part2(input)}")