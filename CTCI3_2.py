#Stack Min
#How would you design a stack which in addition to push and pop has a function "min" that returns the minimum element?
#Push, pop, and min should all operate in O(1) time

#2*X - min element

class Stack:
    def __init__(self):
        self.items = []
        self.minimum = float("inf")

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if self.isEmpty():
            self.minimum = item
            self.items.append(item)
        if item < self.minimum:
            self.items.append(2*item - self.minimum)
            self.minimum = item
        else:
            self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return
        if self.items[-1] > self.minimum:
            return self.items.pop()
        elif self.items[-1] < self.minimum:
            self.minimum = 2*self.minimum - self.items[-1]
            return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def min(self):
        return self.minimum

if __name__ == '__main__':
    mystack = Stack()
    mystack.push(11)
    mystack.push(10)
    mystack.push(5)
    mystack.push(8)
    mystack.push(2)
    print(mystack.min())
    mystack.pop()
    print(mystack.min())