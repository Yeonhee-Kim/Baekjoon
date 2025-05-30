import heapq
import sys
N = int(sys.stdin.readline().strip())
arr = []


for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr))
            
    else:
        heapq.heappush(arr, (num))
