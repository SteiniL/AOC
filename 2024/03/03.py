import re

def readData():
    with open("input.txt") as f:
        return f.read()

def partOne(data):
    matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)
    return sum((int(a) * int(b)) for a, b in matches)

def partTwo(data):
    token = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")
    enabled = True
    result = 0

    for match in token.finditer(data):
        if match.group(0) == 'do()':
            enabled = True
        elif match.group(0) == "don't()":
            enabled = False
        else: 
            if enabled:
                a, b = match.groups()
                result += int(a) * int(b)
    return result

def main(): 
    data = readData()
    print(partOne(data))
    print(partTwo(data))
    return 0

if __name__ == "__main__":
    main()