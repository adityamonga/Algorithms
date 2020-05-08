import random

## In-place
def qsort(arr, start=0, end=None):
    if end == None:
        end = len(arr) - 1

    if end <= start:
        return arr

    pivot = arr[start]
    index = start ## start of unseen elements
    less = start ## start of elements == pivot
    more = end ## start of elements > pivot

    while index <= more:
        if arr[index] < pivot:
            arr[index], arr[less] = arr[less], arr[index]
            index += 1
            less += 1

        elif arr[index] > pivot:
            arr[index], arr[more] = arr[more], arr[index]
            more -= 1

        else:
            index += 1
    qsort(arr, start, less-1)
    qsort(arr, more+1, end)

    return arr

## Makes new lists
# def qsort(arr):
    # if len(arr) <= 1:
    #     return arr
    # else:
    #     pivot = random.choice(arr)
    #     less = []
    #     more = []
    #     for i in arr:
    #         if i < pivot:
    #             less.append(i)
    #         elif i > pivot:
    #             more.append(i)
    #     less = qsort(less)
    #     more = qsort(more)

    #     return less + [pivot] * arr.count(pivot) + more


if __name__ == '__main__':
    arr = [1,2,6,3,9,7]
    arr = random.sample(range(50),50)
    print(arr)
    print(qsort(arr))
    # print(arr)