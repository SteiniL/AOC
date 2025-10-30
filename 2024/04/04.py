def readData():
    with open("input.txt") as f:
        return [x for x in f.read().strip().split()]

def partOne(data):
    rows = len(data)
    cols = len(data[0])
    word = "XMAS"

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

    count = 0

    for r in range(rows):
        for c in range(cols):
            if data[r][c] == word[0]:
                for dr, dc in directions:
                    found = True
                    for i in range(1, len(word)):
                        nr = r + dr * i
                        nc = c + dc * i
                        if not (0 <= nr < rows and 0 <= nc < cols and data[nr][nc] == word[i]):
                            found = False
                            break
                    if found:
                        count += 1
    return count


def partTwo(data):
    word = "MAS"
    rows = len(data)
    cols = len(data[0])

    result = 0
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            if data[r][c] == 'A':
                wordOne = data[r-1][c-1] + data[r][c] + data[r+1][c+1]
                wordTwo = data[r+1][c-1] + data[r][c] + data[r-1][c+1]
                if (wordOne == word or wordOne == word[::-1]) and (wordTwo == word or wordTwo == word[::-1]):
                    result += 1

    return result


def main():
    data = readData()
    print("Part One:", partOne(data))
    print("Part Two:", partTwo(data))

if __name__ == "__main__":
    main()