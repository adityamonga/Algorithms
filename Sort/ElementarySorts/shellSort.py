import random

def shellSort(arr):
	for h in (7,3,1): ## if this series only contains 1, it is insertion sort
		for x in range(len(arr)):
			for y in range(x,0,-1):
				if arr[y] < arr[y-h]:
					arr[y-h], arr[y] = arr[y], arr[y-h]
				else:
					break

	return arr

if __name__ == '__main__':
	print(shellSort(random.sample(range(20), 20)))