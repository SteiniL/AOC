from collections import Counter

def readData():
    left, right = zip(*[map(int, line.split()) for line in open("input.txt")])
    return list(left), list(right)

def partOne(data):
    left = sorted(data[0])
    right = sorted(data[1])
    return sum(abs(x-y) for x, y in zip(left, right))

def partTwo(data):
    freq = Counter(data[1])
    return sum(x * freq[x] for x in data[0])

def main():
    data = readData()
    print(partOne(data))
    print(partTwo(data))

if __name__ == "__main__":
    main()