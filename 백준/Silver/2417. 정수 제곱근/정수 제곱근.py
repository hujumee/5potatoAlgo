import sys

n = int(sys.stdin.readline())

def bin_search(start, end, x):
    while start <= end:
        mid = (start+end) // 2
        if end-start == 1 or x == end**2:
            return end
        elif x == start ** 2:
            return start
        elif x > mid ** 2:
            start = mid
        else:
            end = mid
            
start = 0
end = n
print (bin_search(start, end, n))    