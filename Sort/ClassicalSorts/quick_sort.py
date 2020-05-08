import random

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        
        while low <= high and array[low] <= pivot:
            low += 1

        while low <= high and array[high] >= pivot:
            high -= 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def sort(array, start, end):
    if start >= end:
        return
        
    p = partition(array, start, end)
    sort(array, start, p-1)
    sort(array, p+1, end)

def quick_sort(array):
    random.shuffle(array)
    sort(array, 0, len(array)-1)
    return array

if __name__ == '__main__':
    # print(quick_sort([2,6,41,68,4,45,10]))
    array = [4,2,1,6,5,3]
    array = random.sample(range(20), 20)
    print(array)
    quick_sort(array)
    print(array)