def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    lc, rc = 0, 0
    merged = [None] * (len(left) + len(right))

    while lc < len(left) and rc < len(right):
        if right[rc] < left[lc]:
            merged[lc + rc] = right[rc]
            rc += 1
        else:
            merged[lc + rc] = left[lc]
            lc += 1

    while lc < len(left):
        merged[lc + rc] = left[lc]
        lc += 1

    while rc < len(right):
        merged[lc + rc] = right[rc]
        rc += 1

    return merged

if __name__ == '__main__':
    print(merge_sort(((14, 71), (22, 71), (84, 71), (84, 71), (86, 71))))