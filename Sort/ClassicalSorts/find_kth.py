def find_kth(a, b, size_a, size_b, k):
    if size_a > size_b:
        return find_kth(b, a, size_b, size_a, k)

    if size_a == 0 and size_b > 0:
        return b[k-1]

    if k == 1:
        return min(a[0], b[0])

    i = min(size_a, k//2)
    j = min(size_b, k//2)

    if a[i] < b[j]:
        return find_kth(a[i:], b, size_a - i, size_b, k-i)
    else:
        return find_kth(a, b[j:], size_a, size_b - j, k-j)

if __name__ == '__main__':
    a = [i for i in range(1, 11, 2)]
    b = [i for i in range(2,12, 2)]
    print(a, b)
    print(find_kth(a, b, len(a)-1, len(b)-1, 3))