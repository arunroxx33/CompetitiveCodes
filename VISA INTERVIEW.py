# 1
'''
def findtriplet(arr, reqsum):
    n = len(arr)
    arr.sort()
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        currsum = arr[i]
        
        while left < right:
            tempsum =  currsum + arr[left] + arr[right]
            if tempsum == reqsum:return (arr[i], arr[left], arr[right])
            elif tempsum > reqsum:right -= 1
            else:left += 1
            

    return False

    
l = list(map(int, input().split()))
reqsum = int(input())

print(findtriplet(l, reqsum))


'''

# 2
'''
grid = 0

def printpath(intial, dptable):
    global grid
    
    itr = intial
    
    for j in range(len(dptable[0])):
        print((itr, j) ,' Value : ', grid[itr][j], ' - > ', end = '')
        itr = dptable[itr][j][1]
    
    print('\n\n')
    
    
    

def givemaximumpathsum():
    global grid
    n, m = len(grid), len(grid[0])
        
    dptable = [[(0, 0) for i in range(m)] for j in range(n)]
    
    
    for i in range(n):
        dptable[i][-1] = [grid[i][-1], None]
    
    for j in range(m - 2, -1, -1):
        for i in range(n - 1, -1, -1):
            
            currsum = grid[i][j]
            currans = [-float('inf'), None]
            
            
            for dx in range(max(0, i - 1),min(n,i + 2), 1):
                if currsum + dptable[dx][j + 1][0] > currans[0]:
                    currans = [currsum + dptable[dx][j + 1][0], dx]
                    
            dptable[i][j] = currans[:]

    maximumsum = max(dptable[i][0][0] for i in range(n))

    print("MAXIMUM SUM IS : ", maximumsum)
    
    for i in range(n):
        if dptable[i][0][0] == maximumsum:
            printpath(i, dptable)
    
    

n, m = list(map(int, input().split(' ')))


grid = []

for i in range(n):
    grid.append(list(map(int, input().split())))
    
givemaximumpathsum()


'''




# Final Round - 1

# 1

'''

You have an array.
n = len(arr)
Count the number of pairs where arr[i] >= 2 * arr[j] and i < j.


( Solution )

Step - 1 : Coordinate Compression
Step - 2 : Use Segment/Fenwick Tree to count the pair for current index.


'''


class Node:
    def __init__(self, s, e):
        self.start = s
        self.end = e
        self.val = 0
        self.left = None
        self.right = None

        
def build(nums, l, r):
    newnode = Node(l, r)
    if l == r:
        newnode.val = nums[l]
    else:
        mid = (l + r) // 2
        
        newnode.left = build(nums, l, mid)        
        newnode.right = build(nums, mid + 1, r)
        newnode.val = newnode.left.val + newnode.right.val
    return newnode
        
        
        
def update(root, start, value):
    if root.start == start == root.end:
        root.val += value
    elif root.start <= start and root.end >= start:
        update(root.left, start, value)
        update(root.right, start, value)
        root.val = root.left.val + root.right.val

def query(root, start, end):
    if root.start >= start and root.end <= end:
        return root.val
    elif root.start > end or root.end < start:
        return 0
    else:
        ans1 = query(root.left, start, end)
        ans2 = query(root.right, start, end)
        return ans1 + ans2
        

def compress(l):
    s = set()
    
    
    for i in l:
        s.add(i)
        
    l1 = dict()
    
    ind = 1
    
    for element in sorted(s):
        l1[element] = ind
        ind +=  1
    
    l = [l1[i] for i in l]
    
    return l

    
    
# print(compress(list(map(int, input().split()))))

def count_pairs(arr):
    
    n = len(arr)
    print(arr)    
    arr = compress(arr)
    
    print(arr)
    ans = 0
    
    root = build( [0] * (2 * n + 5), 0, 2 * n + 2)
    last = 0
    for i in arr[::-1]:
        ans += query(root, 0, i)
        update(root, 2 * i, 1)
        
        print(i, ans - last)
        last = ans
        
        
    return ans

    
    
print(count_pairs(list(map(int, input().split()))))
    
    
    
 