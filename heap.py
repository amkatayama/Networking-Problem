# Created by professor 
# Reference for what methods can be used, and how the data structure was implemented

def parent(i):
    return int((i-1)/2)

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

class heap:
    def __init__(self, lst, prios):
        self.lst = list(zip(prios, lst))
        self.n = len(lst)
        self.dct = {}
        self.__heapify__()
        for i in range(self.n):
            self.dct[self.lst[i][1]] = i

    def __swap__(self, i, j):
        ki = self.lst[i][1]
        kj = self.lst[j][1]

        temp = self.lst[i]
        self.lst[i] = self.lst[j]
        self.lst[j] = temp
        self.dct[ki] = j
        self.dct[kj] = i

    def __moveDown__(self, i):
        while True:
            if left(i) >= self.n:
                return i
            else:
                child = self.lst[left(i)]
                ci = left(i)
                if right(i) < self.n and self.lst[right(i)][0] < child[0]:
                    child = self.lst[right(i)]
                    ci = right(i)
                if self.lst[i][0] <= child[0]:
                    return i
                else:
                    self.__swap__(ci, i)
                    i = ci
        return i

    def __moveUp__(self, i):
        while True:
            if i == 0:
                return i
            else:
                p = self.lst[parent(i)]
                pi = parent(i)
                if self.lst[i][0] > p[0]:
                    return i
                else:
                    self.__swap__(pi, i)
                    i = pi
        return i

    def __heapify__(self):
        for i in range(int(self.n/2-1), -1, -1):
            self.__moveDown__(i)

    def __repr__(self):
        return str(self.lst[:self.n])

    def __contains__(self, v):
        return v in self.dct

    def prio(self, v):
        if v in self:
            return self.lst[self.dct[v]][0]
        else:
            return -1

    def decrease_key(self, val, prio):
        i = self.dct[val]
        self.lst[i] = (prio, self.lst[i][1])
        self.dct[val] = self.__moveUp__(i)

    def pop(self):
        res = self.lst[0]
        self.__swap__(0, self.n-1)
        self.n = self.n-1
        self.__moveDown__(0)
        del self.dct[res[1]]
        return res

    def is_empty(self):
        return self.n <= 0


if __name__ == "__main__":
    h = heap(["a","b","c","d","e"], [5,1,4,3,2])
    print(h)
    print(h.pop())
    print(h)
    h.decrease_key("a", 1)
    print(h.pop())
