class MaxHeap:
    def __init__(self):
        self.maxHeap = []

    def get_length(self):
        return len(self.maxHeap)

    def put(self, item):
        self.maxHeap.append(item)
        self.bubble_up()

    def pop(self):
        if self.get_length() == 0:
            raise Exeption('Empty heap')
        if self.get_length() == 1:
            return self.maxHeap.pop()
        max = self.maxHeap[0]
        self.maxHeap[0] = self.maxHeap.pop()
        self.bubble_down()
        return max

    def buildHeap(self, list=[]):
        self.maxHeap = list
        index = self.get_length()//2-1
        while index >=0:
            self.bubble_down(index)
            index -= 1

    def bubble_up(self):
        child = self.get_length() - 1
        parent = self.get_parent(child)
        while child > 0 and self.maxHeap[parent] < self.maxHeap[child]:
            self.swap(parent, child)
            child = parent
            parent = self.get_parent(child)

    def bubble_down(self, parent=0):
        left, right = self.get_children(parent)
        max_child = self.max_child(left, right)
        while max_child > 0 and self.maxHeap[parent] > self.maxHeap[max_child]:
            self.swap(max_child, parent)
            parent = max_child
            left, right = self.get_children(parent)
            max_child = self.max_child(left, right)

    def max_child(self, left, right):
        if left<self.get_length() and right< self.get_length():
            if self.maxHeap[left]> self.maxHeap[right]:
                return left
            else:
                return right
        elif left < self.get_length():
            return left
        else:
            return -1

    def swap(self, i, j):
        self.maxHeap[i], self.maxHeap[j] = self.maxHeap[j], self.maxHeap[i]

    def get_parent(self, child):
        if child % 2 != 0:
            return (child - 1) // 2
        else:
            return (child - 2) // 2

    def get_children(self, parent):
        left = 2 * parent + 1
        right = 2 * parent + 2
        return left, right

mh = MaxHeap()
mh.buildHeap([1,4,7])
print(mh.maxHeap)
