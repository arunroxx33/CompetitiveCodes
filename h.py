from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush,heappop
import math
from collections import *
from functools import reduce,cmp_to_key,lru_cache
import io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# import sys
# input = sys.stdin.readline
 
M = mod = 10**9 + 7 
def factors(n):return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n):return pow(n, mod - 2, mod)
 
def li():return [int(i) for i in input().rstrip().split()]
def st():return str(input().rstrip())[2:-1]
def val():return int(input().rstrip())
def li2():return [str(i)[2:-1] for i in input().rstrip().split()]
def li3():return [int(i) for i in st()]




n, m, w = li()

l = []
for i in range(n):l.append(li())



he = []
if l[0][0] != -1:he.append([0, 0, 0])
visited = {}

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

myset = []


while (n - 1, m - 1) not in visited and he:
    cost, x, y = heappop(he)

    if (x, y) in visited or l[x][y] == -1:continue

    

    if l[x][y] and myset:

        cost = min(cost, l[x][y] + myset[0])

    visited[(x, y)] = cost

    if l[x][y]:

        heappush(myset, cost + l[x][y])
    
    for dx, dy in d:
        if 0 <= dx + x < n and 0 <= dy + y < m and l[dx + x][dy + y] != -1 and (x + dx, dy + y) not in visited:
            heappush(he, [cost + w, x + dx, y + dy])
    # print(he)


he = []

index = [-1,-1]
currcost = float('inf')

for i in range(n):
    for j in range(m):
        if l[i][j] > 0 and (i, j) in visited and currcost > visited[(i, j)]:
            currcost = visited[(i, j)] + l[i][j]
            index = [i, j]

if index != [-1, -1]:

    for i in range(n):
        for j in range(m):
            if l[i][j] > 0:
                heappush(he, [l[i][j] + currcost, i, j])
    
    if l[0][0] != -1:heappush(he, [0, 0 ,0])
    visited = {}
    while he and (n - 1, m - 1) not in visited:
        cost, x, y = heappop(he)

        if (x, y) in visited or l[x][y] == -1:continue

    

        if l[x][y] and myset:

            cost = min(cost, l[x][y] + myset[0])

        visited[(x, y)] = cost

        if l[x][y]:

            heappush(myset, cost + l[x][y])
        
        for dx, dy in d:
            if 0 <= dx + x < n and 0 <= dy + y < m and l[dx + x][dy + y] != -1 and (x + dx, dy + y) not in visited:
                heappush(he, [cost + w, x + dx, y + dy])


if (n - 1, m - 1) not in visited:
    print(-1)
else:print(visited[(n - 1, m - 1)])