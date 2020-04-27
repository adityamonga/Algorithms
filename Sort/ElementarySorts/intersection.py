def intersection(a, b):
    common = set()
    a.sort()
    b.sort()
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            common.add(a[i])
            i += 1
            j += 1

        elif a[i] < b[j]:
            i += 1

        else:
            j += 1

    return common


if __name__ == '__main__':
    a = [2,3,4,5,8]
    b = [5,2,8,9,6, 10]
    print(intersection(a,b))