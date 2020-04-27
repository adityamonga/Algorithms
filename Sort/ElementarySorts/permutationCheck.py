def isPermutation(a, b):
    a.sort()
    b.sort()
    i, j = 0, 0
    if not len(a) == len(b):
        return False

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            return False

    return True

if __name__ == '__main__':
    a = [2,3,4,5, 8]
    b = [5,4,3,2, 8]
    print(isPermutation(a,b))