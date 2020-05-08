import random

def insertionSort(arr):
    for x in range(len(arr)):
        for y in range(x,0,-1):
            if arr[y] < arr[y-1]:
                arr[y-1], arr[y] = arr[y], arr[y-1]
            else:
                break
    return arr

if __name__ == '__main__':
    arr = [5,4,3,2,1,6]
    arr = random.sample(range(15), 15)
    print(insertionSort(arr))
