#Stack of Plates
#implement a data structure SetOfStacks that is composed of several stacks and should create a new stack once the previous once exceeds capacity.

#follow up! implement a function popAt(int index) which performs a pop operation on a specific sub stack

class SetOfStacks:
    def __init__(self,capacity):
        self.stacks = [[]]
        self.capacity = capacity
    def push(self, item):
        if len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            print("previous stack at capacity, creating new stack")
            self.stacks.append([])
            self.stacks[-1].append(item)
    def pop(self):
        if self.stacks[-1] == []:
            del self.stacks[-1]
        return self.stacks[-1].pop()

    def display(self):
        print("printing stacks")
        for x in self.stacks:
            print(x)
        print("-----")

    def popAt(self,index):
        if index >= len(self.stacks):
            print("index out of range")
            return
        popped_value = self.stacks[index].pop()
        if self.stacks[index] != self.stacks[-1]:
            for x in range(index,len(self.stacks)-1):
                self.stacks[x].append( self.stacks[x+1][0] )
                del self.stacks[x+1][0]
            return popped_value
        else:
            return popped_value

if __name__ == '__main__':
    sos = SetOfStacks(2)
    sos.push(2)
    sos.push(3)
    sos.push(1)
    sos.push(4)
    sos.display()
    sos.push(2)
    sos.push(3)
    sos.popAt(0)
    sos.display()
    sos.popAt(2)
    sos.display()