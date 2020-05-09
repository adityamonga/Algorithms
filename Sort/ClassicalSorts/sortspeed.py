import random
import datetime
from timsort import timsort
from merge_sort import merge_sort

def main(func, loops):
    start = datetime.datetime.now()

    for each in range(loops):
        arr = random.sample(range(500), 200)
        func(arr)

    return datetime.datetime.now() - start


if __name__ == '__main__':
    print(main(merge_sort, 500))
    print(main(timsort, 500))
