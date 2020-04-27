## has logical bugs

def sortColors(n):
    i, j = 0, len(n)-1
    curr = 0

    while curr < len(n):
        if color(n[curr]) == 'b':
            swap(n, i, curr)
            i += 1

        elif color(n[curr]) == 'r':
            swap(n, j, curr)
            j -= 1

        curr += 1

    return n

def swap(n, a, b):
    n[a], n[b] = n[b], n[a]

def color(ele):
    return ele
        

if __name__ == '__main__':
    print(sortColors(['b','b','r' ,'b' ,'w' ,'w' ,'r']))