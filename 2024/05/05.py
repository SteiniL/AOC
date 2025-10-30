import math
def readData():
    with open("input.txt") as f:
        data = [x.strip() for x in f.readlines()]

    rules, updates = [x for x in data if '|' in x], [x for x in data if x and '|' not in x]
    rules = [(int(x), int(y)) for x, y in (r.split('|') for r in rules)]
    updates = [[int(x) for x in u.split(',')] for u in updates]

    return rules, updates

def sortUpdates(data):
    correct, incorrect = [], []
    for update in data[1]:
        for rule in data[0]:
            if rule[0] in update and rule[1] in update:
                if not update.index(rule[0]) < update.index(rule[1]):
                    incorrect.append(update)
                    break
        else:
            correct.append(update)
    return correct, incorrect

def partOne(data):
    correct = sortUpdates(data)[0]
    return sum(update[len(update)//2] for update in correct)

def partTwo(data):
    incorrect = sortUpdates(data)[1]
    corrected = []

    #brute force
    for update in incorrect:
        unsorted = True
        while unsorted:
            unsorted = False
            for rule in data[0]:
                if rule[0] in update and rule[1] in update:
                    indexOne = update.index(rule[0])
                    indexTwo = update.index(rule[1])
                    if indexOne > indexTwo:
                        update[indexOne], update[indexTwo] = update[indexTwo], update[indexOne]
                        unsorted = True
                        break
        corrected.append(update)
    return sum(update[len(update)//2] for update in corrected)

def main():
    data = readData()
    print("Part One: ", partOne(data))
    print("Part Two: ", partTwo(data))
    return 0

if __name__ == "__main__":
    main()
    