def readData():
    with open('input.txt') as f:
        return [
            (int(sol), list(map(int, nums.split())))
            for sol, nums in (line.split(":", 1) for line in f if line.strip())
        ]

def testEquation(nums, ops):
    val = nums[0]
    for i in range(len(nums)-1):
        if ops[i] == '0':
            val += nums[i+1]
        elif ops[i] == '1':
            val *= nums[i+1]
    return val

def getBinaryWithLenghth(n, l):
    out = str(bin(n))[2:]
    while len(out) < l:
        out = '0' + out
    return out

def partOne(data):
    out = 0
    for sol, nums in data:
        l = len(nums) - 1
        for mask in range(1 << l):
            val = nums[0]
            for i in range(l):
                if (mask >> (l - 1 - i)) & 1:
                    val *= nums[i+1]
                else:
                    val += nums[i+1]
            if val == sol:
                out += sol
                break
    return out

def concat(a, b):
        pow10 = 1
        x = b
        while x:
            x //= 10
            pow10 *= 10
        return a * pow10 + b

def partTwo(data):
    out = 0
    for sol, nums in data:
        l = len(nums) - 1
        for mask in range(3**l):
            val = nums[0]
            temp = mask
            for i in range(l):
                op = temp % 3
                temp //= 3

                nxt = nums[i+1]
                if op == 0:
                    val += nxt
                elif op == 1:
                    val *= nxt
                else:
                    val = concat(val, nxt)

                if val > sol:
                    break

            if val == sol:
                out += sol
                break
    return out

def main():
    data = readData()
    print('Part One: ' + str(partOne(data.copy())))
    print('Part Two: ' + str(partTwo(data)))
    return 0

if __name__ == "__main__":
    main()