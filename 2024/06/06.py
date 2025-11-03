from collections import Counter

def readData():
    with open("input.txt") as f:
        data = f.read().strip().split("\n")
    return data

def findStartPos(data):
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == '^':
                return (row, col)
    return None

def countX(data):
    x = 0
    for row in data:
        x += row.count('X')
    return x

def partOne(data):
    pos = findStartPos(data)
    direction = '^'
    inScreen = True

    iterations = 0
    while inScreen:
        iterations += 1
        x, y = pos

        # Go UP
        if direction == '^':
            if data[x][y] != '#':
                data[x] = data[x][:y] + 'X' + data[x][y+1:]
                x -= 1
            else:
                x += 1
                y += 1
                direction = '>'

        # Go RIGHT    
        if direction == '>':
            if data[x][y] != '#':
                data[x] = data[x][:y] + 'X' + data[x][y+1:]
                y += 1
            else:
                x += 1
                y -= 1
                direction = 'v'

        # Go DOWN    
        if direction == 'v':
            if data[x][y] != '#':
                data[x] = data[x][:y] + 'X' + data[x][y+1:]
                x += 1
            else:
                x -= 1
                y -= 1
                direction = '<'

        # Go LEFT    
        if direction == '<':
            if data[x][y] != '#':
                data[x] = data[x][:y] + 'X' + data[x][y+1:]
                y -= 1
            else:
                x -= 1
                y += 1
                direction = '^'
                
        
        pos = x, y
        if x < 0 or x > len(data)-1 or y < 0 or y > len(data[0])-1:
            inScreen = False
    return data

DIRS = {'^':(-1,0), '>':(0,1), 'v':(1,0), '<':(0,-1)}
RIGHT = {'^':'>','>':'v','v':'<','<':'^'}

def causes_loop_with_obstacle(data, obs_r, obs_c):
    H = len(data)
    W = len(data[0])
    grid = [list(row) for row in data]

    start = findStartPos(data)
    sr, sc = start
    sd = grid[sr][sc]

    if (sr, sc) == (obs_r, obs_c):
        return False
    grid[obs_r][obs_c] = '#'

    grid[sr][sc] = '.'

    r, c, d = sr, sc, sd
    seen = set()
    while True:
        state = (r, c, d)
        if state in seen:
            return True
        seen.add(state)

        dr, dc = DIRS[d]
        nr= r + dr
        nc = c + dc

        if not (0 <= nr < H and 0 <= nc < W):
            return False

        if grid[nr][nc] == '#':
            d = RIGHT[d]
        else:
            r, c = nr, nc

def partTwo(data):
    H = len(data)
    W = len(data[0])
    start = findStartPos(data)

    sr, sc = start

    count = 0
    for r in range(H):
        for c in range(W):
            if causes_loop_with_obstacle(data, r, c):
                count += 1
    return count

def main():
    data = readData()
    print('Part One: ' + str(countX(partOne(data.copy()))))
    print('Part Two: ' + str(partTwo(data)))
    return 0

if __name__ == "__main__":
    main()