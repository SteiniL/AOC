def readData():
    with open("input.txt") as f:
        return [[int(x) for x in line.strip().split()] for line in f if line.strip()]

def is_safe(row):
    if len(row) < 2:
        return False
    diffs = [a - b for a, b in zip(row, row[1:])]
    return all(1 <= abs(d) <= 3 for d in diffs) and (all(d > 0 for d in diffs) or all(d < 0 for d in diffs))

def partOne(data):
    result = 0
    for row in data:
        if (is_safe(row)):
            result += 1
            continue
    return result  

def partTwo(data):
    result = 0
    for row in data:
        if is_safe(row):
            result += 1
            continue
        for i in range(len(row)):
            new_row = row[:i] + row[i+1:]
            if is_safe(new_row):
                result += 1
                break
    return result

def main():
    data = readData()

    print(partOne(data))
    print(partTwo(data))

if __name__ == "__main__":
    main()