import random

def compare(nuts, bolts, start=0, end=None):
    if end == None:
        end = len(nuts)-1

    if end <= start:
        return

    rnut_index = random.randint(start, end)
    rbolt_index = partition(bolts, nuts[rnut_index], start, end)
    rnut_index = partition(nuts, bolts[rbolt_index], start, end)

    compare(nuts, bolts, start, rnut_index-1)
    compare(nuts, bolts, rnut_index+1, end)

    return nuts, bolts


def partition(arr, pivot, start=0, end=None):

    low = start
    high = end

    while True:

        while low <= high and arr[low] < pivot:
            if arr[low] == pivot:
                arr[low], arr[high] = arr[high], arr[low]
            low += 1

        while low <= high and arr[high] > pivot:
            if arr[high] == pivot:
                arr[low], arr[high] = arr[high], arr[low]
            high -= 1

        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    return low


if __name__ == '__main__':
    # print(compare([2,6,4,8], [8,6,2,4]))
    print(compare(random.sample(range(10), 10), random.sample(range(10), 10)))

