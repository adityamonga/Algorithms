## select kth smallest element
# from quick_sort import partition
import random

def selection(arr, k, start=0, end=None):
    if end == None:
        end = len(arr)-1

    if end <= start:
        return

    while True:
        index = partition(arr, start, end)
        if k == index:
            break
        elif k < index:
            end = index-1
        else:
            start = index+1

    return arr[index]

def partition(arr, start, end):

    pivot = arr[start]
    low = start+1
    high = end

    while True:
        while low <= high and arr[low] <= pivot:
            low += 1

        while low <= high and arr[high] >= pivot:
            high -= 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    arr[start], arr[high] = arr[high], arr[start]

    return high

if __name__ == '__main__':
    # arr = [1,6,3,5,4,8]
    arr = random.sample(range(10,20), 10)
    print(selection(arr, 4))
    print(sorted(arr))
    # print(arr, sorted(arr))


