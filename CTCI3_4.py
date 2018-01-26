#queue via stacks: Implement a queue class which implements a queue using two stacks
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


class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.queueStack = self.stack2

    def add(self,item):
        if self.stack1.isEmpty() and self.stack2.isEmpty():
            self.stack1.push(item)
        else:
            if self.stack1 == self.queueStack:
                self.stack2.push(item)
            else:
                self.stack1.push(item)


    def remove(self):
        if self.stack1.isEmpty() and self.stack2.isEmpty():
            print("queue is empty")
        else:
            if self.queueStack.isEmpty():
                if self.stack1 == self.queueStack:
                    for x in range(0,len(self.stack2.items)):
                        self.queueStack.push(self.stack2.pop())
                else:
                    for x in range(0,len(self.stack1.items)):
                        self.queueStack.push(self.stack1.pop())
                return self.queueStack.pop()

            else:
                return self.queueStack.pop()

    def peek(self):
        if self.isEmpty():
            return "cannot peek, queue is empty"
        if self.queueStack.isEmpty():
            if self.queueStack == self.stack1:
                return self.stack2.items[0]
            else:
                return self.stack1.items[0]
        else:
            return self.queueStack.items[-1]

    def isEmpty(self):
        return self.stack1.isEmpty() and self.stack2.isEmpty()

queue = MyQueue()
queue.add(1)
queue.add(2)
queue.add(3)
queue.add(4)
print(queue.stack1.items)
print(queue.stack2.items)
print(queue.remove())
print(queue.stack1.items)
print(queue.stack2.items)
print(queue.remove())
queue.add(1)
queue.add(2)
print(queue.stack1.items)
print(queue.stack2.items)
print(queue.remove())
print(queue.remove())
print(queue.remove())
print(queue.remove())
print(queue.stack1.items)
print(queue.stack2.items)
print(queue.peek())
queue.add(1)
print(queue.peek())