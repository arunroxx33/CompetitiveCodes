import sys
input = sys.stdin.readline

class Node:
    def __init__(self,s,e):
        self.start=s
        self.end=e
        self.val = 0
        self.left=None
        self.right=None
 
def build(nums,l,r):
    if l == r:
        temp = Node(l,l)
        temp.val = nums[l]
    else:
        mid=(l+r)>>1
        temp=Node(l,r)
        temp.left=build(nums,l,mid)
        temp.right=build(nums,mid+1,r)
        temp.val = max(temp.left.val,temp.right.val)
    return temp

def update(root,start,value):
    if root.start == start == root.end:
        root.val = value
    elif root.start <= start and root.end >= start:
        update(root.left,start,value)
        update(root.right,start,value)
        root.val = max(root.left.val,root.right.val)





def query(root,start,end):
    if root.start>=start and root.end<=end:return root.val
    elif root.start>end or root.end<start:return -float('inf')
    else:
        temp1 = query(root.left,start,end)
        temp2 = query(root.right,start,end)
        return max(temp1,temp2)
        

