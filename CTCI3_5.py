#SortStack write a program to sort a stack such that the smallest items are on the top. you can use an additional
# temporary stack, but you may not copy the elements into any other data structure (such as an array) the stack supports
# the following operations push pop peek and isEmpty.

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)

    def stackSort(self):
        tempStack = Stack()
        while not self.isEmpty():
            temp = self.pop()
            while not tempStack.isEmpty() and tempStack.peek() > temp:
                self.push(tempStack.pop())
            tempStack.push(temp)

        while not tempStack.isEmpty():
            self.push(tempStack.pop())


if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(5)
    stack.push(15)
    stack.push(7)
    stack.display()
    stack.stackSort()
    stack.display()