'''
Fenwick Tree Class

--FireBird23

'''
class Bitree:
    def __init__(self):
        self.bitree = []

    def getsum(self,i):
        s = 0
        i += 1
        while i > 0:
            s += self.bitree[i]
            i -= i&(-i)
        return s

    def sum(self,a,b):
        return self.getsum(b) - self.getsum(a - 1) if a else self.getsum(b)


    def update(self,i,v):
        i += 1
        while i < len(self.bitree):
            self.bitree[i] += v
            i += i&(-i)


    def build(self,arr):
        n = len(arr)
        self.bitree = [0]*(n + 1)
        for i in range(n):self.update(i,arr[i])

# USAGE
# FIRE = Bitree()
# FIRE.build([i for i in range(10)])
# FIRE.sum(1,5)
# FIRE.update(3,5)
