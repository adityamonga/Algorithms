def threesum(data):
    vals = set(data)
    threes = set()
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if -(data[i] + data[j]) in vals:
                valone, valtwo = data[i], data[j]
                threes.add(tuple(sorted([valone, valtwo, -(valone + valtwo)])))
    return threes

if __name__ == '__main__':
    print(threesum([10, 30, -50, 20, -30, -20]))
