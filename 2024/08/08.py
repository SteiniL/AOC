import math
from itertools import combinations
from collections import defaultdict

def readData():
    with open('input.txt') as f:
        return f.read().split()

def getAllFrequencies(data):
    dot = set('.')
    freq = []
    for row in data:
        frquencys = set(row) - dot
        for f in frquencys:
            if f not in freq:
                freq.append(f)
    return freq

def getAllAntennaCoords(frequencies, data):
    coords = defaultdict(list)
    for r, row in enumerate(data):
        for c, val in enumerate(row):
            if val in frequencies:
                coords[val].append((r, c))
    return dict(coords)

def getAllAntinodesPart1(antennas, data):
    R = len(data)
    C = len(data[0])
    antinodes = set()

    for freq, pts in antennas.items():
        for p, q in combinations(pts, 2):
            # external antinodes
            for x, y in ((2*p[0] - q[0], 2*p[1] - q[1]),
                         (2*q[0] - p[0], 2*q[1] - p[1])):
                if 0 <= x < R and 0 <= y < C:
                    antinodes.add((x, y))

            # internal antinodes at 1/3 and 2/3 (only if integer)
            xnum = 2*p[0] + q[0]; ynum = 2*p[1] + q[1]
            if xnum % 3 == 0 and ynum % 3 == 0:
                x, y = xnum // 3, ynum // 3
                if 0 <= x < R and 0 <= y < C:
                    antinodes.add((x, y))

            xnum = p[0] + 2*q[0]; ynum = p[1] + 2*q[1]
            if xnum % 3 == 0 and ynum % 3 == 0:
                x, y = xnum // 3, ynum // 3
                if 0 <= x < R and 0 <= y < C:
                    antinodes.add((x, y))

    return list(antinodes)

def partOne(data):
    allFrequencies = getAllFrequencies(data)
    allAntennaCoords = getAllAntennaCoords(allFrequencies, data)
    allAntinodes = getAllAntinodesPart1(allAntennaCoords, data)

    return len(allAntinodes)

def getAllAntinodesPart2(antennas, data):
    R = len(data)
    C = len(data[0]) if R else 0
    antinodes = set()

    for freq, pts in antennas.items():
        if len(pts) < 2:
            continue
        for (y1, x1), (y2, x2) in combinations(pts, 2):
            dy = y2 - y1
            dx = x2 - x1
            g = math.gcd(abs(dy), abs(dx))
            step_y = dy // g
            step_x = dx // g

            by, bx = y1, x1
            while 0 <= by < R and 0 <= bx < C:
                antinodes.add((by, bx))
                by -= step_y
                bx -= step_x

            fy, fx = y1 + step_y, x1 + step_x
            while 0 <= fy < R and 0 <= fx < C:
                antinodes.add((fy, fx))
                fy += step_y
                fx += step_x

    return antinodes

def partTwo(data):
    allFrequencies = getAllFrequencies(data)
    allAntennaCoords = getAllAntennaCoords(allFrequencies, data)
    allAntinodes = getAllAntinodesPart2(allAntennaCoords, data)
    return len(allAntinodes)

def main():
    data = readData()
    print('Part One: ' + str(partOne(data.copy())))
    print('Part Two: ' + str(partTwo(data)))
    return 0

if __name__ == "__main__":
    main()