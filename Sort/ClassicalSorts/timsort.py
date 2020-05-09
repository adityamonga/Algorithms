import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import random
from ElementarySorts.insertionSort import insertionSort
from merge_sort import merge


def timsort(arr):
    if len(arr) <= 32:
        return insertionSort(arr)

    mid = len(arr) // 2

    left = timsort(arr[:mid])
    right = timsort(arr[mid:])
    return merge(left, right)



if __name__ == '__main__':
    rlist = random.sample(range(100), 100)
    print(rlist)
    print('*'*50)
    print(timsort(rlist))